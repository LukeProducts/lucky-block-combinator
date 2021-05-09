class Minecraft():
    """
    This Python library will help you with crash reports in Minecraft Java Edition, which can be thrown by Lucky Blocks when some block IDs of different Lucky Blocks do not differ.
    This gives an error like "java.lang.IllegalArgumentException: The name lootplusplus:blockid has been registered twice".
    With the help of this library you are able to find out which Lucky Blocks are incompatible with which others, because you don't know that otherwise and save a lot of effort here.
    If you have found a duplicate registration,
    you can also modify a Lucky Block without leaving it away so that you rename the objects and no more errors occur.
    """
    def __init__(self, directory):
        """:param directory: directory in which the Lucky Blocks are located"""
        self.glob_dir = directory if not directory.endswith("/") and not directory.endswith("\\") else directory.rstrip(directory[-1])
        self.found = []
        self.files = []
        self.replaced = []
    def find(self, search, directory_list):
        """
        Searching for minecraft object like block, item, etc. in every readable subfile
        Example:
        Minecraft crash report: "java.lang.IllegalArgumentException: The name lootplusplus:plural_block has been registered twice, for com.tmtravlr.lootplusplus.additions.BlockAdded@306e9bf0 and com.tmtravlr.lootplusplus.additions.BlockAdded@1b2c756a."
        Minecraft is crashing because two Lucky Blocks were assigned the same ID and now you need to change the name "plural_block" to something else.
        Now if you search for the object "plural_block", you will see that in several Lucky Blocks have found the same ID.
        This tells you the compatibility of the Lucky Blocks.
        In this case you will see: [..."/LuckyBlockVideoGames/bow_drops.txt", ...] and [..."/LuckyBlockPlural/bow_drops.txt", ...].
        This informes us that this Lucky Block is not compatible with the plural Lucky Block,
        so you can't play either the Lucky Block plural or the Lucky Block VideoGames,
        so you have to choose one of the two or use the brought replace() function to modify the Lucky Block file to make your game work.
        :param search: object to search for
        :param directory_list: list of Directories to search in [can be generated with the function get_file_dirs()]
        :returns: List of files in which the searched object is present
        """
        import os
        directory_list = [directory if not directory.endswith("/") and not directory.endswith("\\") else directory.rstrip(directory[-1]) for directory in directory_list]
        if type(directory_list) == list:
            if directory_list and all([os.path.exists(i) for i in directory_list]):
                for directory in directory_list:
                    try:
                        with open(directory, "r+") as f:
                            if search in f.read():
                                self.found.append(directory)
                    except:
                        pass
                return self.found
            else:
                raise ValueError(f"{directory_list} is no valid list of directorys")
        else:
            raise ValueError("no list object given")
    def get_file_dirs(self):
        """
        You will get a list of all subfiles of the Lucky Block folder that start with .txt or with .json.
        These are the files that are readable and necessary for the modification of Lucky Blocks
        :return: list of all subfiles into set Lucky Blocks Directory
        """
        import os, zipfile
        if self.glob_dir and os.path.exists(self.glob_dir):
            for maybezip in os.listdir(self.glob_dir):
                if maybezip.endswith(".zip") and maybezip.replace(".zip", "") not in os.listdir(self.glob_dir):
                    with zipfile.ZipFile(self.glob_dir + "/" + maybezip, 'r') as zip_ref:
                        os.mkdir(self.glob_dir + "/" + maybezip.replace(".zip", ""))
                        zip_ref.extractall(self.glob_dir + "/" + maybezip.replace(".zip", ""))
                    os.remove(self.glob_dir + "/" + maybezip)
                elif not maybezip.endswith(".zip") and (maybezip + ".zip") in os.listdir(self.glob_dir):
                    os.remove(self.glob_dir + "/" + maybezip + ".zip")
                else:
                    if not os.path.isdir(self.glob_dir + "/" + maybezip):
                        raise ValueError(f"unknown file format {maybezip}")
            directory = os.listdir(self.glob_dir)
            for Lucky_Block in directory:
                if os.path.isdir(self.glob_dir + "/" +  Lucky_Block):
                    for r, d, f in os.walk(self.glob_dir + "/" + Lucky_Block):
                        for file in f:
                            if '.txt' in file or ".json" in file:
                                self.files.append(os.path.join(r, file).replace('\\', r'/'))
            return self.files
        else:
            raise ValueError(f"Directory \"{self.glob_dir}\" does not exist")
    def replace(self, searchfor, replace_to):
        """
        In order to modify a Lucky Block to make it compatible to others with same Objects you have to change the loot name of these objects
        To execute this function, the files-list must be present in the environment variables with get_file_dirs()
        Not to change the objects name in every Lucky Block, you have to remove at least the other Lucky Block having the same object.
        The script will now change the name of all crucial files in the Lucky Block Folder and change their content searchfor variable to the replace_to variable.
        Minecraft, once you've renamed all duplicate objects, will no longer crash and you will be able to play all possible Lucky Block combinations with each other.
        You don't need to worry about textures.
        They will still work.
        :param searchfor: object to search for
        :param replace_to: object to replace to
        :return: True after successfully process
        """
        if type(searchfor) == str and type(replace_to) == str:
            if self.files:
                for file in self.files:
                    try:
                        with open(file, "r") as f:
                            data = f.read()
                            if searchfor in data:
                                f.close()
                                with open(file, "w") as f:
                                    f.write(data.replace(searchfor, replace_to))
                                self.replaced.append(file)
                    except:
                        pass
                return True
            else:
                raise ValueError("File list not set")
        else:
            raise ValueError("Params have to be strings")

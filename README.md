# Lucky Block Combinator
This Python library will help you with crash reports in Minecraft Java Edition, which can be thrown by Lucky Blocks when some block IDs of different Lucky Blocks do not differ. \
This gives an error like "java.lang.IllegalArgumentException: The name lootplusplus:blockid has been registered twice". \
With the help of this library you are able to find out which Lucky Blocks are incompatible with which others, \
because you don't know that otherwise and save a lot of effort here. \
If you have found a duplicate registration, you can also modify a Lucky Block without leaving it away so that you rename the objects and no more errors occur.

# Installation
```ruby
pip install lucky-block-combinator
```

# Usage

| Function | Description |
| ----- | ----- |
| init(directory)| directory in which the Lucky Blocks are located |
| find(search, directory_list)|Searching for minecraft object like block, item, etc. in every readable subfile  Example: Minecraft crash report: "java.lang.IllegalArgumentException: The name lootplusplus:plural_block has been registered twice, for com.tmtravlr.lootplusplus.additions.BlockAdded@306e9bf0 and com.tmtravlr.lootplusplus.additions.BlockAdded@1b2c756a." Minecraft is crashing because two Lucky Blocks were assigned the same ID and now you need to change the name "plural_block" to something else. Now if you search for the object "plural_block", you will see that in several Lucky Blocks have found the same ID.This tells you the compatibility of the Lucky Blocks.In this case you will see: [..."/LuckyBlockVideoGames/bow_drops.txt", ...] and [..."/LuckyBlockVideoGames/bow_drops.txt", ...]. This informes us that this Lucky Block is not compatible with the plural Lucky Block, so you can't play either the Lucky Block plural or the Lucky Block VideoGames, so you have to choose one of the two or use the brought replace() function to modify the Lucky Block file to make your game work. param search: object to search for, param directory_list: list of Directories to search in [can be generated with the function get_file_dirs()] returns: List of files in which the searched object is present
|get_file_dirs()|You will get a list of all subfiles of the Lucky Block folder that start with .txt or with .json. These are the files that are readable and necessary for the modification of Lucky Blocks, returns: list of all subfiles into set Lucky Blocks Directory|
|replace(searchfor, replace_to)| In order to modify a Lucky Block to make it compatible to others with same Objects you have to change the loot name of these objects To execute this function, the files-list must be present in the environment variables with get_file_dirs(). Not to change the objects name in every Lucky Block, you have to remove at least the other Lucky Block having the same object. The script will now change the name of all crucial files in the Lucky Block Folder and change their content searchfor variable to the replace_to variable. Minecraft, once you've renamed all duplicate objects, will no longer crash and you will be able to play all possible Lucky Block combinations with each other. You don't need to worry about textures. They will still work., param searchfor: object to search for, param replace_to: object to replace to, returns: True after successfully process|
# Examples

1. get_file_dirs()
```python
from lucky_block_combinator.Minecraft import Minecraft
mc = Minecraft("your/path/to/directory/with/all/your/lucky_blocks/in/it")
print(mc.get_file_dirs())

OUTPUT:

['C:/Users/User/lucky_block/TrollLuckyBlock/config/ore_dictionary/additions.txt', ...]
```
2. find(search, directory_list)
```python
from lucky_block_combinator.Minecraft import Minecraft
mc = Minecraft("your/path/to/directory/with/all/your/lucky_blocks/in/it")
directories = mc.get_file_dirs()
print(mc.find("op_box", directories))

OUTPUT:

['C:/Users/User/lucky_block/plural_lucky_block_5.1.0_newrise12/assets/lootplusplus/models/item/plural.op_box.json', ...]
```
3. replace(searchfor, replace_to)
```python
from lucky_block_combinator.Minecraft import Minecraft
mc = Minecraft("your/path/to/directory/with/all/your/lucky_blocks/in/it")
directories = mc.get_file_dirs()
found = mc.find("op_box", directories)
print(mc.replace("op_box", "op_box2")

OUTPUT:

True
```

[![Build Status](https://user-images.githubusercontent.com/73026669/110617122-9c75ad00-8195-11eb-9ba5-422356072776.png)](https://github.com/LukeProducts)

© Copyright by LukeProducts

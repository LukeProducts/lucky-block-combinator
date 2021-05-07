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
| find(search, directory_list)|Searching for minecraft object like block, item, etc. in every readable subfile  Example: Minecraft crash report: "java.lang.IllegalArgumentException: The name lootplusplus:plural_block has been registered twice, for com.tmtravlr.lootplusplus.additions.BlockAdded@306e9bf0 and com.tmtravlr.lootplusplus.additions.BlockAdded@1b2c756a." Minecraft is crashing because two Lucky Blocks were assigned the same ID and now you need to change the name "plural_block" to something else. Now if you search for the object "plural_block", you will see that in several Lucky Blocks have found the same ID.This tells you the compatibility of the Lucky Blocks.In this case you will see: [..."/LuckyBlockVideoGames/bow_drops.txt", ...] and [..."/LuckyBlockVideoGames/bow_drops.txt", ...]. This informes us that this Lucky Block is not compatible with the plural Lucky Block, so you can't play either the Lucky Block plural or the Lucky Block VideoGames, so you have to choose one of the two or use the brought replace() function to modify the Lucky Block file to make your game work. param search: object to search for, param directory_list: list of Directories to search in [can be generated with the function get_file_dirs()] returns: List of files in which the searched object is present|

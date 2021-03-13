# Playlist Manager DOS
A playlist downloader for Beat Saber

# Warning
**The default Path to Beat Saber is set to "C:\\SteamLibrary\\steamapps\\common\\Beat Saber", to change it, edit the json and replace this path with the right one, the path needs to lead to the Beat Saber directory, NOT PLAYLIST OR CUSTOM MAPS ONE**

# DOS ?
Yes, DOS. There isn't any GUI, edition is with commands. I'm really sorry but making a GUI in Python is just a nightmare.

# Feedback
I obviously need feedbacks about bugs, etc... If something went wrong, DM me on discord : Moréo#0001 or open an issue on GitHub.

# How to use
- To use the Playlist Manager, you firstly need to add the path to the Beat Saber folder (as shown in the warning section).

- Then, you can start PlaylistManager.exe and it will check if the path is right. You can disable this verification by changing "checkPath" to false in the settings (but be careful, if you don't respect the way the folder are in the Beat Saber folder, the playlist manager will stop). Then it will scan all the maps that you have (will probably take several minutes).

- Manager will now ask you which playlist you want, either you type a number to select a playlist, either you type "new" to create a new one.

# Create a new playlist
To create a new playlist, you need to type "new" as selected playlist. It will ask infos about the playlist (that you can obviously pass). To add an image, you need to put the jpg or the png in the "Images" folder.

# List of commands :
You need to select a playlist before typing these commands.
## DELETE
  As the name says, this command is to delete a playlist. After you typed this command, it will ask you if you're sure, because it can't be undone (as files don't go in the bin)

## ADDMAP
Not implemented yet 

## REMOVEMAP
Not implemented yet 

## EDITINFO
This command allows you to change infos of a playlist (Title, Author, etc...) **but not the maps inside the playlist**

## DOWNLOAD
This command download the selected playlist

## EXIT
Close Playlist Manager

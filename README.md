# EverQuest Guild Bank Inventory Converter - README

This guide will help you set up and run the Python script that converts your EverQuest guild bank inventory logs into nicely formatted markdown files for your website.

## What This Script Does

This script:
- Reads inventory files from your EverQuest guild banks
- Processes the items, filtering out common or unwanted items
- Converts the inventory into markdown format with clickable links to item database
- Creates organized, sorted lists that are ready for web publishing
- Automatically adds timestamps showing when the inventory was last updated

## Installation Instructions

### Step 1: Install Python

1. Check if you already have Python installed:
   - Press `Win + R` on your keyboard
   - Type `cmd` and press Enter
   - In the black window that appears, type `python --version` and press Enter
   - If you see something like "Python 3.x.x", you already have Python and can skip to Step 2

2. If Python is not installed:
   - Go to [python.org/downloads](https://python.org/downloads)
   - Click the big "Download Python" button (get the latest version)
   - Run the downloaded file
   - **IMPORTANT**: Check the box that says "Add Python to PATH" at the bottom of the installer
   - Click "Install Now"
   - Wait for installation to complete and click "Close"

### Step 2: Download the Script

1. Create a folder where you want to keep the script (e.g., `C:\GuildBankConverter`)
2. Copy the Python script to this folder
3. Make sure the file is named `process_inventory.py`

## Before Running the Script

### Step 1: Create Inventory Files in EverQuest

1. Log into EverQuest with the character who has access to the guild banks
2. For each bank:
   - Open the bank inventory
   - Type `/outputfile Inventory` to save the current inventory to a file
   - This creates a file in your EverQuest directory with the inventory data

3. Rename the inventory files appropriately:
   - Rename the spell bank inventory to `Fgspells-Inventory.txt`
   - Rename the sky items bank inventory to `Fsbank-Inventory.txt`
   - Move these files to the same folder as your script

### Step 2: Edit the Script (Optional)

If you need to customize which items are excluded from the inventory:

1. Right-click on the `process_inventory.py` file
2. Select "Edit with Notepad" or just "Edit"
3. Look for these lines:
   ```python
   excluded_items = ['Empty', 'Backpack', 'Elemental Grimoire', 'A Worn Candle', 'Hand Made Backpack', 'Currency', 'Bread Cakes*', 'Skin of Milk', 'Large Sewing Kit']
   excluded_ids = ['0', '17005', '17880']
   ```

4. Add or remove items from these lists as needed
5. Save the file (File > Save or press Ctrl+S)

## Running the Script

### Method 1: Direct Double-Click

1. Simply double-click the `process_inventory.py` file
2. A command window will appear briefly and then close when processing is complete
3. Two new files will be created in the same folder:
   - `spells.md` - Contains the formatted spell inventory
   - `sky.md` - Contains the formatted sky items inventory

### Method 2: Command Prompt (If Double-Click Doesn't Work)

1. Right-click in the folder where your script is located while holding Shift
2. Select "Open command window here" or "Open PowerShell window here"
3. Type `python process_inventory.py` and press Enter
4. You'll see confirmation messages that the files were processed

## What the Output Files Look Like

The script creates markdown files that include:
- A properly formatted header (front matter) for your website
- A last update date showing when the inventory was last modified
- A sorted list of all items with links to an item database (pqdi.cc)
- Item counts for multiple items (shown as "x2", "x3", etc.)

## Troubleshooting

If the script doesn't work:
- Make sure Python is installed correctly
- Verify that your inventory files exist and are named correctly
- Check that the inventory files are in the correct format (tab-separated data)
- Make sure you have permission to write to the output directory

## Need Help?

If you continue to have issues:
- Take a screenshot of any error messages
- Check that your inventory files are being created properly in EverQuest
- Verify that the output from `/outputfile Inventory` matches the expected format

This script will help you maintain an up-to-date and accessible inventory of your guild banks on your website!

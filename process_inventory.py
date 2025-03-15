import os
from datetime import datetime
from collections import Counter

def process_text_data(text_data, is_spell_inventory):
    lines = text_data.strip().split('\n')
    item_counter = Counter()
    excluded_items = ['Empty', 'Backpack', 'Elemental Grimoire', 'A Worn Candle', 'Hand Made Backpack', 'Currency', 'Bread Cakes*', 'Skin of Milk', 'Large Sewing Kit']
    excluded_ids = ['0', '17005', '17880']
    
    # Skip the first line
    for line in lines[1:]:
        parts = line.split('\t')
        if len(parts) > 3:
            item_name = parts[1].strip()
            item_id = parts[2].strip()
            
            # Check if the item should be excluded
            if item_name not in excluded_items and item_id not in excluded_ids:
                if is_spell_inventory:
                    # For spells, we just count occurrences
                    item_counter[(item_name, item_id)] += 1
                else:
                    # For bank items, we sum the counts
                    count = int(parts[3].strip())
                    item_counter[(item_name, item_id)] += count
    
    output_lines = []
    for (item_name, item_id), count in item_counter.items():
        if count > 1 or not is_spell_inventory:
            output_lines.append(f'[{item_name}](https://www.pqdi.cc/item/{item_id}) x{count}')
        else:
            output_lines.append(f'[{item_name}](https://www.pqdi.cc/item/{item_id})')
    
    # Sort the output lines alphabetically by item name
    output_lines.sort(key=lambda x: x.split('[')[1].lower())
    return output_lines

def write_to_markdown_file(output_lines, output_file_path, front_matter, last_update):
    with open(output_file_path, 'w') as f:
        f.write(front_matter + '\n\n')  # Write front matter at the top of the file
        f.write(f'### Last Update: {last_update}\n\n')  # Add last update date as an H3 header
        for line in output_lines:
            f.write(line + '\n\n')  # Add an extra newline after each item

def process_inventory_files(file_names):
    for file_name in file_names:
        with open(file_name, 'r') as file:
            input_data = file.read()
        
        is_spell_inventory = 'Fgspells-Inventory.txt' in file_name
        processed_data = process_text_data(input_data, is_spell_inventory)
        
        # Get the date modified of the source file and format it to only include the date
        mod_time = os.path.getmtime(file_name)
        last_update = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
        
        if 'Fgspells-Inventory.txt' in file_name:
            output_file = 'spells.md'
            front_matter = """---
layout: page
title: Spell Bank
cover-img: /assets/img/spells.webp
subtitle: List of Spells in the guild bank
---
### Speak with Dihat if you wish to make a withdraw."""
        elif 'Fsbank-Inventory.txt' in file_name:
            output_file = 'sky.md'
            front_matter = """---
layout: page
title: Sky Bank
cover-img: /assets/img/sky.webp
subtitle: List of Plane of Sky items in the guild bank
---
### Speak with Dihat if you wish to make a withdraw."""
        else:
            print(f"Unrecognized file name: {file_name}")
            continue
        
        write_to_markdown_file(processed_data, output_file, front_matter, last_update)
        print(f"Processed {file_name} and wrote output to {output_file}")

# Example usage
inventory_files = ['Fgspells-Inventory.txt', 'Fsbank-Inventory.txt']
process_inventory_files(inventory_files)

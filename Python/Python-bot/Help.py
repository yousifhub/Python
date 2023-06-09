import discord
import json

def help(category=None):
    with open('commands.json', 'r') as file:
        command_categories = json.load(file)

    embed = discord.Embed(title='Help', color=0xff0000)

    if category:
        if category in command_categories:
            commands = command_categories[category]
            if category == 'events':
                command_list = '\n'.join([f"{command['name']} - {command['description']}" for command in commands])
            else:
                command_list = '\n'.join([f"`!{command['name']}` - {command['description']}" for command in commands])
            embed.add_field(name=category, value=command_list, inline=False)
        else:
            return "Category not found."

    else:
        for category, commands in command_categories.items():
            if category == 'events':
                command_list = '\n'.join([f"{command['name']} - {command['description']}" for command in commands])
            else:
                command_list = '\n'.join([f"`!{command['name']}` - {command['description']}" for command in commands])
            embed.add_field(name=category, value=command_list, inline=False)

    return embed
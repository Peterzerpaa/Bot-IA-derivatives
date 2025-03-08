import discord
from discord.ext import commands
import os
from model import IA

permisos = discord.Intents.default()
permisos.message_content = True

bot = commands.Bot(command_prefix="$", intents=permisos)

@bot.event
async def on_ready():
    print("El bot está en línea")

@bot.command()
async def bienvenidos(ctx):
    await ctx.send("Bienvenido a tu bot \n Aquí puedes encontrar diferente información sobre la contaminación")

@bot.command()
async def descomposicion(ctx, *, objeto: str):
    tiempo_descomposicion = {
        "papel": "2 a 6 meses",
        "carton": "2 meses",
        "vidrio": "4000 años"
    }
    
    objeto = objeto.lower()
    if objeto in tiempo_descomposicion:
        await ctx.send(f"El tiempo de descomposición de {objeto} es: {tiempo_descomposicion[objeto]}")
    else:
        await ctx.send("No tengo información sobre ese elemento")

@bot.command()
async def check(ctx):
    if not ctx.message.attachments:
        await ctx.send("No has adjuntado ningún archivo")
        return

    # Asegurar que la carpeta ./img existe
    if not os.path.exists("./img"):
        os.makedirs("./img")

    for file in ctx.message.attachments:
        name_file = file.filename
        file_path = f"./img/{name_file}"
        await file.save(file_path)

        # Llamar a la función IA y enviar el resultado
        resultado = IA(img_path=file_path, model_path="./keras_model.h5", label_path="./labels.txt")
        await ctx.send(resultado)
bot.run("MTI4NzQxNjYxNTk0Mzc5ODg4NQ.G69OUz.9nYuhONqw5GWzoceiT-mkBE0Tkq1lKVj-r669I")
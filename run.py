from highrise.__main__ import BotDefinition, main, import_module, arun
import time

room_id = "630b3ee87e9f9cf7d9257c4a"
bot_token = "3d3e7f3dea69d81c8e3f0714a06de30f165c9721bfcdde89ef06e082c9de1f98"
bot_file = "main"
bot_class = "MyBot"
coordinates = {
        'x': 12,
        'y': 0.5,
        'z': 7,

if __name__ == "__main__":
  definitions = [
	  BotDefinition(
	    getattr(import_module(bot_file), bot_class)(),
      room_id, 
			bot_token)]  # More BotDefinition classes can be added to the definitions list
  while True:
    try:
      arun(main(definitions))
    except Exception as e:
      # Print the full traceback for the exception
      import traceback
      print("Caught an exception:")
      traceback.print_exc()  # This will print the full traceback       
      time.sleep(10)       
      continue

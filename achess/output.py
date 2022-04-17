import accessible_output2.outputs.auto

speaker = accessible_output2.outputs.auto.Auto()

def say(text):
	global speaker
	speaker.output(text)
	
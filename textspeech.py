from text_to_speech import save

text = "Hello, World! Welcome to My Profile."
language = "en"  # Specify the language (IETF language tag)
output_file1 = "hello_world.mp3"  # Specify the output file (only accepts .mp3)

save(text, language, file=output_file1, slow=True)
# Custom Module 1: Data Generation (telemetry.py)
def telemetry_generator(seed, name, artist):
    raw_stream = [seed * 2, len(name) * 5, "CORRUPTED", len(artist) * 2]
    for value in raw_stream:
        yield value
        
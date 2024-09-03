# [ Task 1 ]

# Format list
def format_itineraries(itineraries):
    formatted_itineraries = []

    for index, (traveler_name, origin, destination) in enumerate(itineraries, start=1):
        formatted_itinerary = f"Itinerary {index}: {traveler_name} - From {origin} to {destination}"
        formatted_itineraries.append(formatted_itinerary)

    return "\n".join(formatted_itineraries)

# Pass list of Tuples
flight_itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(format_itineraries(flight_itineraries))
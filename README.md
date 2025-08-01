# 🗺️ Australia Map Location Learning Game

This Python-based project that helps users learn the **states and cities of Australia** through a turtle graphics-based interface. It challenges users to identify locations on a map and rewards correct answers by marking them directly on the map. The project uses **file handling**, **event-driven input**, and **graphical positioning** via Turtle, and promotes experiential learning through repetition and visual feedback.

---

## 🎓 Educational Purpose

- 🌍 Learn and recall **Australian geography** — cities and states.
- 🧠 Enhance memory through **interactive guessing and visual reinforcement**.
- 🗂️ Automatically creates a list of **missed locations** for further study.

---

## 🧠 Key Features

- 📍 Interactive guessing of cities/states in Australia
- 🗺️ Correct guesses stamped directly on the Australian map
- 📄 CSV-based recording of missed or unknown places for further study
- 🎨 Turtle-based graphical interface with visual feedback
- 🧑‍🏫 "Save the City" mode allows users to **add new locations** dynamically

---

## 🎨 Gameplay  Output

Below are sample outputs of Game:

<img width="400" alt="au_state_game" src="https://github.com/user-attachments/assets/bff21a77-af53-4c60-b2f7-9d1e0f40d89a" />

---

## 📌 How It Works

1. The user is shown a **blank map of Australia**.
2. Prompted to **guess a city or state name**.
3. If the guess is correct and matches existing data:
   - The name is **stamped on the map** at its location.
4. The user can type `"Exit"` to stop the game.
5. Upon exiting, the program:
   - Compares guessed names with the full dataset.
   - **Creates a text file** with the names of missed locations.
   - This can be used for future revision.

---

## 🎯 Gameplay Overview

- Enter the name of an Australian **state or major city**.
- If correct:
  - It appears on the map at its correct location.
- If incorrect:
  - Try again, or type `"Exit"` to quit.
- On exit:
  - A `missed_locations.txt` file is generated for review.

---

## 🔧 Core Functionalities

### ✅ `get_location_coordinates(x, y)`
- Allows the user to click a point and assign a **name to that coordinate**.
- Useful for **data collection or custom labeling**.
- Stores data in `au_city.csv` in the format: `name, x, y`.

### ✅ `set_location_coordinates()`
- Loads the coordinates from `au_city.csv`.
- Displays the city/state names at their respective (x, y) positions on the map.

---

## 🖥️ System Requirements

- Python 3.x
- Standard library only (uses `turtle`, `csv`, `pandas`)

---

## 📁 File Structure

```text
australia-map-game/
├── main.py               # Main game loop and user interaction
├── au_city.csv           # Data file with city/state names and coordinates
├── au_map.gif     # Background map of Australia
├── missed_locations.txt  # Output file with unguessed locations
├── README.md             # Project documentation
```

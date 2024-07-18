# Traducciones

## Ruby Snippet
### El prompt fue:
Traduce este código a python:

```ruby
def menu ()
  menu_string = "1. Show Menu\n"
  menu_string += "2. Add Numbers\n"
  menu_string += "3. Subtract Numbers\n"
  menu_string += "4. Quit\n"
  return menu_string
end

# Main Program Starts

system "clear" # Clear the screen
choice = 0

while choice < 4 do
  puts menu()
  choice = gets.to_i

  if choice == 1
    system "clear"
  elsif choice == 2
    puts "\n\nAdd Some Numbers\n\n"
  elsif choice == 3
    puts "\n\nSubtract some Numbers\n\n"
  else
  end
end

## La respuesta fue:
## Traducción a python
import os

def menu():
    menu_string = "1. Show Menu\n"
    menu_string += "2. Add Numbers\n"
    menu_string += "3. Subtract Numbers\n"
    menu_string += "4. Quit\n"
    return menu_string

# Main Program Starts

os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
choice = 0

while choice < 4:
    print(menu())
    choice = int(input())

    if choice == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
    elif choice == 2:
        print("\n\nAdd Some Numbers\n\n")
    elif choice == 3:
        print("\n\nSubtract some Numbers\n\n")
    else:
        pass


## Javascript/NodeJS snippet
## El prompt fue:
Traduce este código a python:

const generateUUID = () =>
  ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, c =>
    (
      c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
    ).toString(16)
  );
## La respuesta fue:
## Traducción a python

import uuid

def generate_uuid():
    return str(uuid.uuid4())


## Golang snippet
## El prompt fue:
Traduce este código a python:
package main

import "fmt"

func ReverseString(s string) string {
  r := []rune(s)
  for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
    r[i], r[j] = r[j], r[i]
  }
  return string(r)
}

## La respuesta fue:
## Traducción a python
def reverse_string(s):
    return s[::-1]


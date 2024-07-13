"""
Write python code to generate Init function of GPIO for AVR
"""
def generate_gpio_init(port, pin, direction, initial_state):
    # Validate direction
    if direction not in ['INPUT', 'OUTPUT']:
        raise ValueError("Direction must be 'INPUT' or 'OUTPUT'")
    
    # Validate initial state
    if initial_state not in ['LOW', 'HIGH']:
        raise ValueError("Initial state must be 'LOW' or 'HIGH'")

    # Generate DDR and PORT register names based on port
    ddr_register = f'DDR{port}'
    port_register = f'PORT{port}'

    # Generate the C code for the initialization function
    code = f'''
#include <avr/io.h>

void GPIO_init(void) {{
    // Set pin direction
    if (direction == 'OUTPUT') {{
        {ddr_register} |= (1 << {pin});
    }} else {{
        {ddr_register} &= ~(1 << {pin});
    }}
    
    // Set initial state
    if (initial_state == 'HIGH') {{
        {port_register} |= (1 << {pin});
    }} else {{
        {port_register} &= ~(1 << {pin});
    }}
}}
'''

    return code

# Example usage
port = 'B'
pin = 3
direction = 'OUTPUT'
initial_state = 'HIGH'

generated_code = generate_gpio_init(port, pin, direction, initial_state)
print(generated_code)

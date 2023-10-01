const newUserDiv = document.getElementById('addUser');

// Function to add a new child
function add_child(newUserDiv, id) {
    // Append a new person input
    newUserDiv.appendChild(new_username(id + 1));
    
    // Remove the event listener from the current input
    const currentInput = document.getElementsByName(`username${id}`)[0];
    if (currentInput) {
        const eventFunction = currentInput.eventFunction;
        if (eventFunction) {
            currentInput.removeEventListener('input', eventFunction);
        }
    }
}

// Function to create a new person input
function new_username(id) {
    const newInput = document.createElement('input');
    
    // Add classes to the new input
    newInput.classList.add('text-[20px]', 'sm:text-[30px]', 'md:text-[40px]', 'lg:text-[50px]', 'bg-[#212121]', 
                           'border-[3px]', 'border-green-600', 'rounded-[10px]', 'mb-[30px]', 'px-[5px]');
    newInput.placeholder = 'Add Username';
    newInput.maxLength = 150;
    newInput.name = `username${id}`;
    newInput.required = false
    
    if (id < 10) {
    // Define the event listener function
    const eventFunction = () => add_child(newUserDiv, id);
    newInput.eventFunction = eventFunction;
    
    // Add the event listener to the new input
    newInput.addEventListener('input', eventFunction);
    }
    
    return newInput;
}

// Initial setup
const initialInput = document.getElementsByName('username1')[0];
if (initialInput) {
    const eventFunction = () => add_child(newUserDiv, 1);
    initialInput.eventFunction = eventFunction;
    initialInput.addEventListener('input', eventFunction);
}

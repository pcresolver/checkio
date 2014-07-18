__author__ = 'Steve'
# This makes the queue a First-In-First-Out (FIFO) data structure. In a FIFO data structure, the first element added to the queue will be the first one to be removed.
# This is equivalent to the requirement that once a new element is added, all elements that were added before have to be removed before the new element can be removed.

def letter_queue(commands):
    queue = [] #used to store the queue as it is being built
    for command in commands:
        action = command[:2] # first two chars of command uniquely identifies push or pop
        if action == "PU":
            queue.append(command[-1]) #add the last char to the end of the queue
        elif queue != []: # check that the list is not empty
            queue.pop(0) # remove the first element in the list - default value removes the last
        print(queue)
    return "".join(queue) # joining the list 'queue' with an empty string converts the list to a string

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"

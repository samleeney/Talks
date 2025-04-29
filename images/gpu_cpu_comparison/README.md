# GPU vs CPU Operations Comparison Images

These images were created for a presentation slide titled "Why is it harder to write code for GPUs".

## Images Description

### 1. CPU Operations (`cpu_operations.png`)

This image visually represents the comprehensive set of operations available on CPUs:

- **Arithmetic Operations**: Basic operations (add, subtract, multiply, divide) and complex math operations (sqrt, sin/cos, log/exp, power)
- **Control Flow Operations**: Various branching and flow control (if/else, branch, jump, function call, return, loop, switch)
- **Memory Operations**: Diverse memory access patterns (load, store, cache read/write, prefetch, memory barrier)
- **Special Purpose Operations**: System-level operations (system call, I/O operations, interrupt, privileged instructions, virtualization)

### 2. GPU Operations (`gpu_operations.png`)

This image illustrates the more limited set of operations available on GPUs:

- **Basic Arithmetic**: Simple operations (add, subtract, multiply, divide) with their symbols
- **Vector/Matrix Operations**: Specialized vector operations (vector add, vector multiply, dot product, cross product)
- **Simple Branching**: Limited branching capabilities with performance penalty indicators (!)
- **Limited Memory Operations**: Restricted memory access (load, store, shared memory)
- **SIMT Constraint**: Visual representation of the Single Instruction, Multiple Thread constraint, showing how all threads must execute the same instruction simultaneously

## Key Differences Highlighted

These images effectively communicate why GPU programming is more challenging than CPU programming by showing:

1. The reduced operation set available on GPUs
2. The performance penalties associated with branching operations on GPUs
3. The SIMT constraint that requires all threads to execute the same instruction
4. The specialized nature of GPU operations focused on parallel computation

## Usage in Presentation

These images can be included in the presentation slide titled "Why is it harder to write code for GPUs" to provide a clear visual comparison between CPU and GPU programming models.
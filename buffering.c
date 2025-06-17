#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 1024  // Define the size of the buffer

typedef struct {
    FILE *file;
    char *buffer;
    size_t buffer_size;
    size_t buffer_index;
} CustomBuffer;

// Initialize the custom buffer
CustomBuffer* init_custom_buffer(FILE *file, size_t buffer_size) {
    CustomBuffer *cb = (CustomBuffer*)malloc(sizeof(CustomBuffer));
    if (cb == NULL) {
        perror("Failed to allocate memory for CustomBuffer");
        exit(EXIT_FAILURE);
    }
    cb->file = file;
    cb->buffer_size = buffer_size;
    cb->buffer = (char*)malloc(buffer_size);
    if (cb->buffer == NULL) {
        perror("Failed to allocate memory for buffer");
        free(cb);
        exit(EXIT_FAILURE);
    }
    cb->buffer_index = 0;
    return cb;
}

// Write data to the custom buffer
void custom_write(CustomBuffer *cb, const char *data, size_t length) {
    size_t remaining = length;
    const char *ptr = data;

    while (remaining > 0) {
        size_t space_left = cb->buffer_size - cb->buffer_index;
        size_t copy_size = (remaining < space_left) ? remaining : space_left;

        memcpy(cb->buffer + cb->buffer_index, ptr, copy_size);
        cb->buffer_index += copy_size;
        ptr += copy_size;
        remaining -= copy_size;

        if (cb->buffer_index == cb->buffer_size) {
            // Flush the buffer to the file
            fwrite(cb->buffer, 1, cb->buffer_size, cb->file);
            cb->buffer_index = 0;
        }
    }
}

// Flush any remaining data in the buffer to the file
void custom_flush(CustomBuffer *cb) {
    if (cb->buffer_index > 0) {
        fwrite(cb->buffer, 1, cb->buffer_index, cb->file);
        cb->buffer_index = 0;
    }
}

// Free the custom buffer
void free_custom_buffer(CustomBuffer *cb) {
    if (cb) {
        if (cb->buffer) {
            free(cb->buffer);
        }
        free(cb);
    }
}

int main() {
    FILE *file = fopen("example.txt", "w");
    if (file == NULL) {
        perror("Failed to open file");
        return EXIT_FAILURE;
    }

    CustomBuffer *cb = init_custom_buffer(file, BUFFER_SIZE);

    // Write data to the custom buffer
    custom_write(cb, "This is a test.", strlen("This is a test."));
    custom_write(cb, " Another line of text.", strlen(" Another line of text."));

    // Flush any remaining data in the buffer to the file
    custom_flush(cb);

    // Free the custom buffer
    free_custom_buffer(cb);

    fclose(file);
    return 0;
}


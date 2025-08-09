#include <regex.h>
#include <stdio.h>

int main() {
    regex_t regex;
    const char *pattern = "([A-Za-z]+) ([0-9]+)";  // Match "word number"
    const char *text = "Hello 123 world 456";
    
    // Compile regex
    if (regcomp(&regex, pattern, REG_EXTENDED)) {
        printf("Regex compilation failed\n");
        return 1;
    }
    
    // Prepare for matches (we want 3 groups: full + 2 submatches)
    regmatch_t matches[3];
    
    // Execute regex
    if (regexec(&regex, text, 3, matches, 0) == 0) {
        printf("Match found!\n");
        
        // Print matched groups
        for (int i = 0; i < 3; i++) {
            if (matches[i].rm_so == -1) break;  // No more groups
            
            int start = matches[i].rm_so;
            int end = matches[i].rm_eo;
            printf("Group %d: %.*s\n", i, end-start, text+start);
        }
    } else {
        printf("No match found\n");
    }
    
    regfree(&regex);
    return 0;
}

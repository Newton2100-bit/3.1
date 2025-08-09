#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define a structure
struct Person {
    char name[50];
    int age;
    float salary;
};

// Define a structure that contains another structure
struct Employee {
    struct Person info;
    int employee_id;
    char department[30];
};

int main() {
    // Example 1: Direct member access using dot operator (.)
    printf("=== Direct Member Access (.) ===\n");
    
    struct Person person1;
    strcpy(person1.name, "John Doe");
    person1.age = 30;
    person1.salary = 50000.50;
    
    printf("Person 1 Details:\n");
    printf("Name: %s\n", person1.name);
    printf("Age: %d\n", person1.age);
    printf("Salary: %.2f\n\n", person1.salary);
    
    // Example 2: Indirect member access using arrow operator (->)
    printf("=== Indirect Member Access (->) ===\n");
    
    struct Person *person2 = malloc(sizeof(struct Person));
    strcpy(person2->name, "Jane Smith");
    person2->age = 28;
    person2->salary = 55000.75;
    
    printf("Person 2 Details:\n");
    printf("Name: %s\n", person2->name);
    printf("Age: %d\n", person2->age);
    printf("Salary: %.2f\n\n", person2->salary);
    
    // Example 3: Mixed usage with nested structures
    printf("=== Mixed Usage with Nested Structures ===\n");
    
    struct Employee emp1;
    strcpy(emp1.info.name, "Alice Johnson");
    emp1.info.age = 35;
    emp1.info.salary = 65000.00;
    emp1.employee_id = 1001;
    strcpy(emp1.department, "Engineering");
    
    printf("Employee 1 (direct access):\n");
    printf("Name: %s\n", emp1.info.name);
    printf("Age: %d\n", emp1.info.age);
    printf("Salary: %.2f\n", emp1.info.salary);
    printf("Employee ID: %d\n", emp1.employee_id);
    printf("Department: %s\n\n", emp1.department);
    
    // Example 4: Pointer to nested structure
    struct Employee *emp2 = malloc(sizeof(struct Employee));
    strcpy(emp2->info.name, "Bob Wilson");
    emp2->info.age = 42;
    emp2->info.salary = 70000.25;
    emp2->employee_id = 1002;
    strcpy(emp2->department, "Marketing");
    
    printf("Employee 2 (pointer access):\n");
    printf("Name: %s\n", emp2->info.name);
    printf("Age: %d\n", emp2->info.age);
    printf("Salary: %.2f\n", emp2->info.salary);
    printf("Employee ID: %d\n", emp2->employee_id);
    printf("Department: %s\n\n", emp2->department);
    
    // Example 5: Function that takes structure pointer
    printf("=== Function with Structure Pointer ===\n");
    void printPersonInfo(struct Person *p) {
        printf("Function - Person Info:\n");
        printf("Name: %s\n", p->name);
        printf("Age: %d\n", p->age);
        printf("Salary: %.2f\n", p->salary);
    }
    
    printPersonInfo(person2);
    printf("\n");
    
    // Example 6: Demonstrating equivalence
    printf("=== Demonstrating Equivalence ===\n");
    printf("Using -> operator: %s\n", person2->name);
    printf("Using * and . : %s\n", (*person2).name);
    printf("Both are equivalent!\n\n");
    
    // Example 7: Array of structures
    printf("=== Array of Structures ===\n");
    struct Person people[3];
    
    // Using dot operator for array elements
    strcpy(people[0].name, "Person A");
    people[0].age = 25;
    people[0].salary = 40000.0;
    
    strcpy(people[1].name, "Person B");
    people[1].age = 30;
    people[1].salary = 45000.0;
    
    strcpy(people[2].name, "Person C");
    people[2].age = 35;
    people[2].salary = 50000.0;
    
    printf("People Array:\n");
    for(int i = 0; i < 3; i++) {
        printf("%d. Name: %s, Age: %d, Salary: %.2f\n", 
               i+1, people[i].name, people[i].age, people[i].salary);
    }
    printf("\n");
    
    // Example 8: Pointer arithmetic with structures
    printf("=== Pointer Arithmetic with Structures ===\n");
    struct Person *ptr = people;  // Point to first element
    
    printf("Using pointer arithmetic:\n");
    for(int i = 0; i < 3; i++) {
        printf("%d. Name: %s, Age: %d, Salary: %.2f\n", 
               i+1, (ptr + i)->name, (ptr + i)->age, (ptr + i)->salary);
    }
    
    // Clean up dynamically allocated memory
    free(person2);
    free(emp2);
    
    return 0;
}

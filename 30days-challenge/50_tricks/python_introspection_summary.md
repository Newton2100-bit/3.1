# Python Introspection Methods & Default Attributes Summary

## **Main Introspection Methods**

| Method | What It Shows | Returns | Works On | Simple Description |
|--------|---------------|---------|-----------|-------------------|
| `locals()` | Local variables in current scope | Dictionary | Functions/methods | "What's on my desk right now?" |
| `globals()` | Global/module-level variables | Dictionary | Anywhere | "What's in the main storage room?" |
| `vars(obj)` | Object's stored data/attributes | Dictionary | Objects with `__dict__` | "What data does this thing have?" |
| `dir(obj)` | All available names (methods, attributes) | List | Any object | "What can this thing do?" |
| `type(obj)` | Exact type of object | Type object | Any object | "What exactly is this?" |
| `isinstance(obj, type)` | Check if object is of certain type | Boolean | Any object | "Is this a [type]?" (smarter than type) |
| `hasattr(obj, 'name')` | Check if object has attribute | Boolean | Any object | "Does this have [attribute]?" |
| `getattr(obj, 'name')` | Get attribute value by name | Any | Any object | "Give me the [attribute] from this" |
| `setattr(obj, 'name', val)` | Set attribute value by name | None | Any object | "Set [attribute] to [value]" |
| `callable(obj)` | Check if object can be called | Boolean | Any object | "Can I run this?" |
| `id(obj)` | Memory address of object | Integer | Any object | "Where is this stored in memory?" |

## **Python Default Attributes (Dunder Attributes)**

### **Object Identity & Type**
| Attribute | Purpose | Simple Description | Example |
|-----------|---------|-------------------|---------|
| `__class__` | Object's class | "What kind of thing am I?" | `"hello".__class__` → `<class 'str'>` |
| `__dict__` | Object's attribute storage | "My personal data storage" | `obj.__dict__` → `{'name': 'Alice'}` |
| `__module__` | Module where class was defined | "Which file am I from?" | `MyClass.__module__` → `'__main__'` |
| `__name__` | Name of class/function | "What's my name?" | `str.__name__` → `'str'` |
| `__doc__` | Documentation string | "My help text" | `len.__doc__` → `'Return the length...'` |

### **String Representation**
| Attribute | Purpose | Simple Description | Example |
|-----------|---------|-------------------|---------|
| `__str__()` | Human-readable string | "How should I look to users?" | `str(obj)` calls this |
| `__repr__()` | Developer-friendly string | "How should I look to programmers?" | `repr(obj)` calls this |
| `__format__()` | Custom formatting | "How should I look in f-strings?" | `f"{obj:custom}"` calls this |

### **Comparison Operations**
| Attribute | Purpose | Simple Description | Example |
|-----------|---------|-------------------|---------|
| `__eq__(other)` | Equal comparison | "Am I equal to other?" | `obj1 == obj2` |
| `__lt__(other)` | Less than | "Am I smaller than other?" | `obj1 < obj2` |
| `__gt__(other)` | Greater than | "Am I bigger than other?" | `obj1 > obj2` |
| `__le__(other)` | Less than or equal | "Am I smaller or equal?" | `obj1 <= obj2` |
| `__ge__(other)` | Greater than or equal | "Am I bigger or equal?" | `obj1 >= obj2` |
| `__ne__(other)` | Not equal | "Am I different from other?" | `obj1 != obj2` |

### **Math Operations**
| Attribute | Purpose | Simple Description | Example |
|-----------|---------|-------------------|---------|
| `__add__(other)` | Addition | "How do I add with other?" | `obj1 + obj2` |
| `__sub__(other)` | Subtraction | "How do I subtract other?" | `obj1 - obj2` |
| `__mul__(other)` | Multiplication | "How do I multiply with other?" | `obj1 * obj2` |
| `__len__()` | Length/size | "How big am I?" | `len(obj)` |
| `__bool__()` | Boolean conversion | "Am I truthy or falsy?" | `bool(obj)` or `if obj:` |

### **Container Operations**
| Attribute | Purpose | Simple Description | Example |
|-----------|---------|-------------------|---------|
| `__getitem__(key)` | Get item by key/index | "Give me item at [key]" | `obj[key]` |
| `__setitem__(key, val)` | Set item by key/index | "Set [key] to [value]" | `obj[key] = val` |
| `__contains__(item)` | Check if item exists | "Do I contain [item]?" | `item in obj` |
| `__iter__()` | Make object iterable | "How to loop through me?" | `for x in obj:` |

### **Object Lifecycle**
| Attribute | Purpose | Simple Description | Example |
|-----------|---------|-------------------|---------|
| `__init__(self, ...)` | Constructor | "How to create me?" | `obj = MyClass()` |
| `__del__(self)` | Destructor | "How to clean up when I'm deleted?" | When object is garbage collected |
| `__call__(self, ...)` | Make object callable | "How to run me like a function?" | `obj()` |

## **Alternative Methods & Their Relationships**

| Instead of... | Use... | Why Better? |
|---------------|--------|-------------|
| `obj.__class__` | `type(obj)` | More explicit |
| `type(obj) == SomeClass` | `isinstance(obj, SomeClass)` | Handles inheritance |
| `obj.__dict__['attr']` | `getattr(obj, 'attr')` | Handles missing attributes gracefully |
| `obj.__dict__['attr'] = val` | `setattr(obj, 'attr', val)` | More consistent |
| `'attr' in obj.__dict__` | `hasattr(obj, 'attr')` | Works even without `__dict__` |
| Manual attribute checking | `vars(obj)` | Shows all attributes at once |
| Guessing what methods exist | `dir(obj)` | Shows everything available |

## **Quick Reference Examples**

### **Object Investigation Combo:**
```python
def investigate(obj):
    print(f"Type: {type(obj)}")
    print(f"ID: {id(obj)}")
    print(f"Callable: {callable(obj)}")
    print(f"Dir: {dir(obj)[:5]}...")  # First 5 items
    if hasattr(obj, '__dict__'):
        print(f"Vars: {vars(obj)}")
```

### **Safe Attribute Access:**
```python
# Instead of risking errors:
# value = obj.some_attr  # Might crash

# Use safe methods:
if hasattr(obj, 'some_attr'):
    value = getattr(obj, 'some_attr')
else:
    value = "Not found"

# Or with default:
value = getattr(obj, 'some_attr', 'default_value')
```

### **Dynamic Object Manipulation:**
```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")

# Dynamic attribute setting:
attributes = {'age': 25, 'city': 'NYC'}
for attr, value in attributes.items():
    setattr(p, attr, value)

# Check what we have:
print(vars(p))  # {'name': 'Alice', 'age': 25, 'city': 'NYC'}
```

## **Memory Aid**

**"The 5 W's of Python Objects":**

1. **WHO** are you? → `type(obj)`, `isinstance()`
2. **WHAT** can you do? → `dir(obj)`, `callable()`  
3. **WHAT** do you have? → `vars(obj)`, `hasattr()`
4. **WHERE** are you? → `id(obj)`
5. **WHY** do you exist? → `obj.__doc__`

**Common Patterns:**
- **Exploring**: `dir()` → see what's available
- **Inspecting**: `vars()` → see what's stored  
- **Accessing**: `getattr()` → get something safely
- **Checking**: `hasattr()` → verify before accessing
- **Comparing**: `isinstance()` → check type safely
import logging

# Set up formatters
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

# 1. ROOT LOGGER (top of hierarchy)
root_logger = logging.getLogger()  # Empty string = root
root_handler = logging.FileHandler('root.log')
root_handler.setFormatter(formatter)
root_logger.addHandler(root_handler)
root_logger.setLevel(logging.DEBUG)

# 2. PARENT LOGGER
parent_logger = logging.getLogger('myapp')
parent_handler = logging.FileHandler('parent.log')
parent_handler.setFormatter(formatter)
parent_logger.addHandler(parent_handler)
parent_logger.setLevel(logging.DEBUG)

# 3. CHILD LOGGER
child_logger = logging.getLogger('myapp.database')
child_handler = logging.FileHandler('child.log')
child_handler.setFormatter(formatter)
child_logger.addHandler(child_handler)
child_logger.setLevel(logging.DEBUG)

# 4. GRANDCHILD LOGGER
grandchild_logger = logging.getLogger('myapp.database.connection')
grandchild_handler = logging.FileHandler('grandchild.log')
grandchild_handler.setFormatter(formatter)
grandchild_logger.addHandler(grandchild_handler)
grandchild_logger.setLevel(logging.DEBUG)

print("=== PROPAGATION DEMO ===")
print("When we log to grandchild, it propagates UP the hierarchy:")
print("grandchild -> child -> parent -> root")
print()

# Log a message from the grandchild
grandchild_logger.error("Database connection failed!")

print("Check these files - the message appears in ALL of them:")
print("- grandchild.log (its own handler)")
print("- child.log (propagated to parent)")
print("- parent.log (propagated to grandparent)")
print("- root.log (propagated to root)")
print()

# Demonstrate hierarchy
print("=== HIERARCHY DEMONSTRATION ===")
parent_logger.warning("This appears in parent.log and root.log")
child_logger.info("This appears in child.log, parent.log, and root.log")

print("\n=== STOPPING PROPAGATION ===")
print("Setting propagate=False on child logger...")

# Stop propagation
child_logger.propagate = False

print("Now logging to child - it will NOT propagate up!")
child_logger.critical("This ONLY appears in child.log")

print("\nFiles to check:")
print("- child.log (has the message)")
print("- parent.log (does NOT have the message)")
print("- root.log (does NOT have the message)")

# Turn propagation back on
child_logger.propagate = True
print("\nTurning propagation back on...")
child_logger.error("This propagates again!")

print("\n=== SUMMARY ===")
print("Propagation means:")
print("1. Messages travel UP the hierarchy")
print("2. Each level's handlers get the message")
print("3. You can stop propagation with propagate=False")
print("4. Root logger catches everything (unless propagation is stopped)")

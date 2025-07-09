import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from itertools import combinations

# Define plant types and their feature ranges
plant_types = {
    'Corn': {
        'height': [150, 300],      # cm
        'leaf_length': [60, 120],  # cm
        'stem_diameter': [2, 4]    # cm
    },
    'Potato': {
        'height': [30, 80],        # cm
        'leaf_length': [15, 35],   # cm
        'stem_diameter': [0.5, 1.5] # cm
    },
    'Grass': {
        'height': [5, 25],         # cm
        'leaf_length': [3, 15],    # cm
        'stem_diameter': [0.1, 0.5] # cm
    }
}

# Parameters
train_num = 200
test_num = 100  # optional
plant_names = list(plant_types.keys())

# Create empty dataset
dataset = []

print("Generating plant dataset...")

# Step 1: Generate approximately train_num/3 samples for each plant type
samples_per_plant = train_num // 3
remaining_samples = train_num - (samples_per_plant * 3)

for plant_name in plant_names:
    plant_config = plant_types[plant_name]
    
    # Generate samples for this plant type
    for _ in range(samples_per_plant):
        sample = {}
        
        # Generate features
        sample['height'] = random.uniform(plant_config['height'][0], plant_config['height'][1])
        sample['leaf_length'] = random.uniform(plant_config['leaf_length'][0], plant_config['leaf_length'][1])
        sample['stem_diameter'] = random.uniform(plant_config['stem_diameter'][0], plant_config['stem_diameter'][1])
        sample['label'] = plant_name
        
        dataset.append(sample)

# Step 2: Fill remaining rows with mislabeled data
for _ in range(remaining_samples):
    # Randomly select a plant type
    true_plant = random.choice(plant_names)
    plant_config = plant_types[true_plant]
    
    # Generate features for the true plant
    sample = {}
    sample['height'] = random.uniform(plant_config['height'][0], plant_config['height'][1])
    sample['leaf_length'] = random.uniform(plant_config['leaf_length'][0], plant_config['leaf_length'][1])
    sample['stem_diameter'] = random.uniform(plant_config['stem_diameter'][0], plant_config['stem_diameter'][1])
    
    # Mislabel it (cyclically shift)
    true_index = plant_names.index(true_plant)
    mislabeled_index = (true_index + 1) % len(plant_names)
    sample['label'] = plant_names[mislabeled_index]
    
    dataset.append(sample)

# Step 3: Randomly shuffle the dataset
random.shuffle(dataset)

# Convert to DataFrame
df = pd.DataFrame(dataset)
df = df.reset_index(drop=True)

print(f"Dataset created with {len(df)} samples")
print(f"Label distribution:")
print(df['label'].value_counts())

# Step 4: Save to CSV files
# Features
feature_data = df[['height', 'leaf_length', 'stem_diameter']]
feature_data.to_csv('potato_train_data.csv', index=False)

# Labels
label_data = df[['label']]
label_data.to_csv('potato_train_label.csv', index=False)

print("\nFiles saved:")
print("- potato_train_data.csv (features)")
print("- potato_train_label.csv (labels)")

# Step 5: Map string labels to integers
label_mapping = {'Corn': 0, 'Potato': 1, 'Grass': 2}
df['label_encoded'] = df['label'].map(label_mapping)

# Step 6: Create scatter plots for each pair of features
features = ['height', 'leaf_length', 'stem_diameter']
feature_pairs = list(combinations(features, 2))

# Set up colors for different classes
colors = {'Corn': 'red', 'Potato': 'blue', 'Grass': 'green'}

# Create subplots
fig, axes = plt.subplots(1, len(feature_pairs), figsize=(15, 5))
if len(feature_pairs) == 1:
    axes = [axes]

for i, (feature1, feature2) in enumerate(feature_pairs):
    ax = axes[i]
    
    # Plot each class with different colors
    for plant_name in plant_names:
        plant_data = df[df['label'] == plant_name]
        ax.scatter(plant_data[feature1], plant_data[feature2], 
                  c=colors[plant_name], label=plant_name, alpha=0.7)
    
    ax.set_xlabel(feature1.replace('_', ' ').title())
    ax.set_ylabel(feature2.replace('_', ' ').title())
    ax.set_title(f'{feature1.replace("_", " ").title()} vs {feature2.replace("_", " ").title()}')
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Additional analysis
print("\nDataset Statistics:")
print(df.describe())

print("\nFeature ranges by plant type:")
for plant_name in plant_names:
    plant_data = df[df['label'] == plant_name]
    print(f"\n{plant_name}:")
    print(f"  Height: {plant_data['height'].min():.1f} - {plant_data['height'].max():.1f} cm")
    print(f"  Leaf Length: {plant_data['leaf_length'].min():.1f} - {plant_data['leaf_length'].max():.1f} cm")
    print(f"  Stem Diameter: {plant_data['stem_diameter'].min():.2f} - {plant_data['stem_diameter'].max():.2f} cm")

# Create a comprehensive visualization
plt.figure(figsize=(12, 8))

# Create a 2x2 subplot layout
plt.subplot(2, 2, 1)
for plant_name in plant_names:
    plant_data = df[df['label'] == plant_name]
    plt.scatter(plant_data['height'], plant_data['leaf_length'], 
               c=colors[plant_name], label=plant_name, alpha=0.7)
plt.xlabel('Height (cm)')
plt.ylabel('Leaf Length (cm)')
plt.title('Height vs Leaf Length')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 2)
for plant_name in plant_names:
    plant_data = df[df['label'] == plant_name]
    plt.scatter(plant_data['height'], plant_data['stem_diameter'], 
               c=colors[plant_name], label=plant_name, alpha=0.7)
plt.xlabel('Height (cm)')
plt.ylabel('Stem Diameter (cm)')
plt.title('Height vs Stem Diameter')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 3)
for plant_name in plant_names:
    plant_data = df[df['label'] == plant_name]
    plt.scatter(plant_data['leaf_length'], plant_data['stem_diameter'], 
               c=colors[plant_name], label=plant_name, alpha=0.7)
plt.xlabel('Leaf Length (cm)')
plt.ylabel('Stem Diameter (cm)')
plt.title('Leaf Length vs Stem Diameter')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(2, 2, 4)
# Distribution of labels
label_counts = df['label'].value_counts()
plt.bar(label_counts.index, label_counts.values, color=[colors[plant] for plant in label_counts.index])
plt.xlabel('Plant Type')
plt.ylabel('Count')
plt.title('Distribution of Plant Types')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\nWampus World Plant Classification Dataset Generation Complete!")
print("This dataset simulates the challenge of identifying plant types from observable features,")
print("similar to how agents in Wampus World must identify hidden elements from sensor readings.")

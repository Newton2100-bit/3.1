class DataProcessor:
    def __init__(self, data_sources):
        self.data_sources = data_sources
    
    def combine_data(self):
        # Combine multiple data sources
        return list(zip(*self.data_sources))
    
    def process_parallel(self, *processors):
        # Apply different processors to different data sources
        results = []
        for data, processor in zip(self.data_sources, processors):
            results.append([processor(item) for item in data])
        return results

# Usage
processor = DataProcessor([
    [1, 2, 3, 4],
    [10, 20, 30, 40],
    [100, 200, 300, 400]
])

combined = processor.combine_data()
print(combined)  # [(1, 10, 100), (2, 20, 200), (3, 30, 300), (4, 40, 400)]

# Process with different functions
results = processor.process_parallel(
    lambda x: x * 2,      # Double first list
    lambda x: x + 5,      # Add 5 to second list
    lambda x: x / 10      # Divide third list by 10
)
print(results)  # [[2, 4, 6, 8], [15, 25, 35, 45], [10.0, 20.0, 30.0, 40.0]]

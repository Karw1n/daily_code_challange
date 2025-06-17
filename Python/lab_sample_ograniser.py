# Coddy Daily Challeng Lab Sample Organizer
# Coddy.tech DC 17/06/2025
'''
Lab Sample Organizer
Create a function named analyze_samples that receives sample_ids, start_index, and end_index as its parameters.

The function simulates a scientist organizing typification samples in a laboratory. It should sort the sample IDs, then reverse a specific subset of the sorted samples.

Follow these steps:

Sort the entire array of sample IDs in ascending order.
Reverse the order of samples between start_index and end_index (inclusive).
Return the final arranged array of sample IDs.
Parameters:

sample_ids (list of int): An array of integers representing unique sample IDs.
start_index (int): The starting index of the subset to be reversed.
end_index (int): The ending index of the subset to be reversed.
The function returns a list of integers representing the final arranged array of sample IDs.
'''

# Function recieves a list of samples as well as a start_index and end_index
# 1. Sort the arry of samples in asc order
# 2. Reverse the order of samples between start_index and end_index (inclusive)
# 3. Return the final arranged array of sample ids

def analyze_samples(sample_ids, start_index, end_index):
    # 1. Sort
    sample_ids.sort()
    # 2. I'm going to extract the sublist
    # As inclusive +1 is needed for end
    extract = sample_ids[start_index:end_index+1]
    # Reverse this list
    extract.sort(reversed)
    # Putting it back into the original
    for i in range(len(extract)):
        sample_ids[i+start_index] = extract[i]
    # 3. Returning the samples
    return sample_ids
        
# Coddy's solution. Pretty much identical but the recombination was simpler.
# A very good way to do it via slicing
def analyze_samples_soltion(sample_ids, start_index, end_index):
    # Step 1: Sort the entire array of sample IDs in ascending order
    sorted_samples = sorted(sample_ids)
    
    # Step 2: Reverse the order of samples between start_index and end_index (inclusive)
    subset = sorted_samples[start_index:end_index+1]
    subset.reverse()
    
    # Step 3: Construct the final arranged array
    final_arranged = sorted_samples[:start_index] + subset + sorted_samples[end_index+1:]
    
    # Return the final arranged array of sample IDs
    return final_arranged
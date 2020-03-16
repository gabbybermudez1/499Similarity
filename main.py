import os
import json
from winnowing import WinnowedDoc

# Reflect this in configurations
ROOT = "C:/Users/gabby/Documents/School/CISC_499/student_data/subset_students"


def jaccard_coefficient(doc1_fp, doc2_fp):
    intersection = [fingerprint for fingerprint in doc1_fp if fingerprint in doc2_fp]
    intersection = len(intersection)
    # union = len(doc1_fp) + len(doc2_fp) - intersection
    denominator = min(len(doc1_fp) , len(doc2_fp) )
    return (intersection / denominator) * 100


def return_file_location(filename, directory):
    '''
    return_file_location returns a path to a given file given some subdirectory. This function will traverse a directory and its subdirectories
    to find the given file. 

    Parameters
    ----------
    filename : str
        String representation of a file name that we want to find

    directory : str
        a directory where we will search recursively for the file
    
    Returns
    -------
    path: str
        path leading to a given file
    
    '''
    for current_dir, dir_names, file_names in os.walk(directory):
        if filename in file_names:
            path = os.path.join(current_dir, filename).replace("\\", "/")
            return path


with open("config.json") as cfg_file:
    cfg = json.load(cfg_file)


# ------ Configurations --------
assignment_name = cfg["assignment_name"]
assignment_files = cfg["assignment_files"]

k_gram_size = cfg["k_gram_size"]
window_size = cfg["window_size"]
use_rolling = cfg["use_rolling_hash"]

students = os.listdir(ROOT)



all_submissions = {}


def generate_fingerprints_all():
    for net_id in students:
        all_submissions[net_id] = {}
        student_dir = os.path.join(ROOT, net_id, assignment_name).replace("\\", '/')
        for assignment_file in assignment_files:
            path = return_file_location(assignment_file, student_dir)
            if path is not None:
                with open(path) as document:
                    contents = document.read()
                all_submissions[net_id][assignment_file] = WinnowedDoc(contents, k_gram_size, window_size, use_rolling).fingerprints

generate_fingerprints_all()
print("--- Generated Fingerprints ---")


# # Compare all fingerprints
with open("similarity_report.txt", "w") as similarity_report:
    for file in assignment_files:
        similarity_report.write("\n========================\n")
        similarity_report.write(file + "\n")
        similarity_report.write("========================\n")
        for i in range(len(students)):
            for j in range(i + 1, len(students)):
                if (all_submissions[students[i]].get(file) is not None) and (all_submissions[students[j]].get(file) is not None ):
                    similarity = jaccard_coefficient(all_submissions[students[i]].get(file), all_submissions[students[j]].get(file))
                    if 25.0 < similarity:
                        similarity_report.write("Student " + students[i] + " and  Student " + students[j] + " have a similarity score of " + str(similarity) + "\n")










# if(15 < similarity):
#     with open("similarity_report.txt", "w") as similarity_report:
#         similarity_report.write("This was plagiarised. Similarity rating was: " + str(similarity))

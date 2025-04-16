import pandas as pd
import os
import json

# def read_json(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#         df = pd.DataFrame(data['results'])
#         return df
#     except FileNotFoundError:
#         print(f"Error file not found")
#         return None
#     except json.JSONDecodeError:
#         print(f"Error could not decode")
#         return None
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return None

def read_all_json_files(dir_path):
    pass
    all_files = []
    for filename in os.listdir(dir_path):
        if filename.endswith(".json"):
            file_path = os.path.join(dir_path, filename)
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    if isinstance(data, list):
                        for record in data:
                            record['source'] = filename
                            all_files.append(record)
                    elif isinstance(data, dict):
                        if 'results' in data and isinstance(data['results'], list):
                            for record in data['results']:
                                record['source'] = filename
                                all_files.append(record)
                        else:
                            data['source'] = filename
                            all_files.append(data)
                    else:
                        print(f"Skipping '{filename}' as not .json")
            except FileNotFoundError:
                print(f"Error file not found")
                return None
            except json.JSONDecodeError:
                print(f"Error could not decode")
                return None
            except Exception as e:
                print(f"Unexpected error: {e}")
                return None
    return pd.DataFrame(all_files)
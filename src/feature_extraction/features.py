def extract_features(image_path):
    print("Extracting features from:", image_path)
    return {"image": image_path}


if __name__ == "__main__":
    extract_features("results/drone.jpeg")

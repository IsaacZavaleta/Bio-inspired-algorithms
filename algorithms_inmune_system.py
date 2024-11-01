import numpy as np
import random

def generate_data(n_samples, anomaly_ratio, n_features):
    normal_data = np.random.normal(loc=0, scale=1, size=(int(n_samples * (1 - anomaly_ratio)), n_features))
    anomaly_data = np.random.normal(loc=5, scale=1, size=(int(n_samples * anomaly_ratio), n_features))
    return np.vstack((normal_data, anomaly_data))

def newAntibody(n_features):
    return np.random.normal(loc=0, scale=1, size=n_features)

def calculateAffinity(antibody, sample):
    distance = np.linalg.norm(antibody - sample)
    return 1 / (1 + distance)

def clone_and_mutate(antibodies, data, n_features, mutation_rate):
    new_population = []
    for antibody in antibodies:
        if random.random() < mutation_rate:
            mutation_vector = np.random.normal(0, 0.5, n_features)
            antibody = antibody + mutation_vector
        new_population.append(antibody)
    return new_population

def evaluate_population(antibodies, data, anomaly_threshold):
    detections = []
    for sample in data:
        max_affinity = max([calculateAffinity(antibody, sample) for antibody in antibodies])
        if max_affinity < anomaly_threshold:
            detections.append(sample)
    return detections

def immune_anomaly_detection(data,n_antibodies,n_features, mutation_rate, n_generations,anomaly_threshold):
    antibodies = [newAntibody(n_features) for _ in range(n_antibodies)]
    
    for generation in range(n_generations):
        population_affinity = [(antibody, max([calculateAffinity(antibody, sample) for sample in data])) for antibody in antibodies]
        antibodies = sorted(population_affinity, key=lambda x: x[1], reverse=True)
        best_antibodies = [antibody[0] for antibody in antibodies[:n_antibodies // 2]]

        antibodies = clone_and_mutate(best_antibodies, data, n_features, mutation_rate)

        detections = evaluate_population(antibodies, data, anomaly_threshold)
        print(f"Iteraccion {generation + 1}:\n\tSe detectaron {len(detections)} anomalías.")

        if len(detections) == 0:
            print("No se encontraron mas anomalías.")
            break


def main():
    #Config
    n_samples = 8
    n_antibodies = 15         
    n_features = 8            
    mutation_rate = 0.2       
    n_generations = 35        
    anomaly_threshold = 0.6
    anomaly_ratio=0.3   

    data = generate_data(n_samples, anomaly_ratio, n_features)
    immune_anomaly_detection(data,n_antibodies,n_features, mutation_rate, n_generations,anomaly_threshold)


if __name__ == '__main__':
    main()


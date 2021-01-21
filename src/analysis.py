# Third party imports
import matplotlib.pyplot as plt
# My imports
import helpers

def analyze_segment_count():
    print('We are going to collect all the data located in ml_h3n2/sample_data/*.fasta')
    sample_data = helpers.get_all_data("../sample_data", ".fasta")
    print(f'Collected {len(sample_data)} unique strains')

    segment_count={'PB2':0, 'PB1':0, 'PA':0, 'HA':0, 'NP':0, 'NA':0, 'MP':0, 'NS':0, 'HE':0, 'P3':0}
    for strain in sample_data.values():
        for key in strain.segments:
            segment_count[key] += 1

    print('Found the following number of occurences for each segment:')
    print(segment_count)

    plt.bar(range(len(segment_count)), list(segment_count.values()), align='center')
    plt.xticks(range(len(segment_count)), list(segment_count.keys()))
    plt.title('# of Occurrences per Segment')
    plt.ylabel('# of Segments')
    plt.xlabel('Segment Name')
    plt.savefig('../figures/segment_count')
    print('Figure saved to ml_h3n2/figures/segment_count.png')
    plt.show()
    print(f'We can see that {segment_count["HA"]} of {len(sample_data)} samples include the hemaggluttinin (HA) segment.')

def main():
    analyze_segment_count()

if __name__ == "__main__":
    main()

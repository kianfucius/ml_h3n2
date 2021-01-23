# Python imports
import argparse
import os
# Third party imports
import matplotlib.pyplot as plt
# My imports
import helpers

def analyze_segment_count(datapath, ext):
    # Collect data
    print('Collecting data from ml_h3n2/sample_data/*.fasta')
    sample_data = helpers.get_all_data(directory=datapath, extension=ext)
    print(f'Collected {len(sample_data)} unique strains')

    # Count segments
    segment_count={'PB2':0, 'PB1':0, 'PA':0, 'HA':0, 'NP':0, 'NA':0, 'MP':0, 'NS':0, 'HE':0, 'P3':0}
    for strain in sample_data.values():
        for key in strain.segments:
            segment_count[key] += 1
    print()
    print('Found the following number of occurences for each segment:')
    print(segment_count)
    print()

    # Set graph data
    plt.bar(range(len(segment_count)), list(segment_count.values()), align='center')
    plt.xticks(range(len(segment_count)), list(segment_count.keys()))
    # Set graph titles and labels
    plt.title('# of Occurrences per Segment\nInternational data up to 01-22-2021')
    plt.ylabel('# of Segments')
    plt.xlabel('Segment Name')
    # Generate graph
    plt.savefig('../figures/segment_count')
    print('Figure saved to ml_h3n2/figures/segment_count.png')
    plt.show()
    print(f'We can see that {segment_count["HA"]} of {len(sample_data)} samples include the hemaggluttinin (HA) segment.')
    print()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default='../sample_data', type=dir_path,
        help="Path to directory containing virus data.")
    parser.add_argument('-e', default='.fasta', type=is_extension,
        help="File extension for data files.")

    return parser.parse_args()

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        argparse.ArgumentError(f'Invalid path {string}')

def is_extension(string):
    if string[0] == '.' and string[1:].isalpha():
        return string
    else:
        argparse.ArgumentError(f'Invalid extension {string}')

def main():
    parsed_args = parse_arguments()

    analyze_segment_count(parsed_args.p, parsed_args.e)

if __name__ == "__main__":
    main()

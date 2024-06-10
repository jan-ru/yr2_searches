import matplotlib.pyplot as plt
import bibtexparser


def parse_bib_file(bib_file):
    with open(bib_file, 'r', encoding='utf-8') as file:
        bib_database = bibtexparser.load(file)
    return bib_database.entries


def plot_timeline(articles):
    years = []
    for article in articles:
        try:
            # Extract the year from the 'year' field
            year = int(article['year'])
            years.append(year)
        except KeyError:
            pass

    # Plot the timeline
    plt.figure(figsize=(10, 5))
    plt.hist(years, bins=[edge - 0.5 for edge in range(min(years),
                                                       max(years) + 2)],
                                                       color='skyblue',
                                                       edgecolor='black')
    plt.title('Timeline of Publications\nn={}'.format(len(articles)))
    plt.ylabel('Number of Articles')
    plt.xticks(range(min(years), max(years) + 2))

    # Set y-axis ticks to integer values
    plt.yticks(range(int(min(plt.gca().get_ylim())), 
                     int(max(plt.gca().get_ylim())) + 1))
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    bib_file = '../MySelection.bib'  # Replace with the path to your .bib file
    articles = parse_bib_file(bib_file)
    plot_timeline(articles)

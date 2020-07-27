import argparse
import csv
from collections import defaultdict


class SoccerLeague:
    def split_data(self, input_file):
        x = input_file
        matches = []
        for row in x:
            match = [i.rstrip().rsplit(' ', 1) for i in row]
            matches.append(match)
        return matches

    def compare_scores(self, input_data):
        unsorted_log = defaultdict(int)

        for game in self.split_data(input_data):
            opponent1_name = game[0][0]
            opponent2_name = game[1][0]
            opponent1_score = game[0][1]
            opponent2_score = game[1][1]

            if opponent1_score > opponent2_score:
                unsorted_log[opponent1_name] += 3
                unsorted_log[opponent2_name] += 0

            elif opponent1_score == opponent2_score:
                unsorted_log[opponent1_name] += 1
                unsorted_log[opponent2_name] += 1

        return unsorted_log

    def sort_results(self, input_data):
        log = self.compare_scores(input_data)
        rankings = sorted(log.items(), key=lambda kv: (-kv[1], kv[0]))
        return rankings

    def rank_teams(self, input_data):
        final_standings = ''
        rankings = self.sort_results(input_data)
        previous_pts = None
        for indx, (team, points) in enumerate(rankings, 0):
            if points != previous_pts:
                indx += 1
                previous_pts = points   
            
            if points == 1:
                points_suffix = "pt"
            else:
                points_suffix = "pts"

            final_standings += f'{indx}. {team} {points} {points_suffix}\n'
        print(final_standings)
        # I'm returning 'final_standings' to test the 'rank_teams' method.
        return final_standings


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()
    match_results = csv.reader(args.file)
    sl = SoccerLeague()
    sl.rank_teams(match_results)
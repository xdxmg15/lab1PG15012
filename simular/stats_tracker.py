from collections import defaultdict


class StatsTracker:

    def __init__(self):

        self.champions = defaultdict(int)

        self.finalists = defaultdict(int)

        self.group_qualifications = defaultdict(int)

    def update(

        self,
        result
    ):

        # CHAMPION

        champion = result[
            'champion'
        ]

        self.champions[
            champion
        ] += 1

        # FINALISTS

        for team in result[
            'finalists'
        ]:

            self.finalists[
                team
            ] += 1

        # GROUP QUALIFIERS

        for slot, data in result[
            'qualified'
        ].items():

            # ONLY 1st/2nd PLACE

            if not (

                slot.startswith('1')
                or
                slot.startswith('2')
            ):

                continue

            team_name = data[
                'team'
            ]

            self.group_qualifications[
                team_name
            ] += 1

    def print_summary(

        self,
        simulations
    ):

        print('\n===== WORLD CUP SUMMARY =====\n')

        print('--- Champions ---')

        for team, count in sorted(

            self.champions.items(),

            key=lambda x: x[1],

            reverse=True
        ):

            probability = (
                count
                /
                simulations
            ) * 100

            print(

                f'{team}: '
                f'{probability:.2f}%'
            )

        print('\n--- Finalists ---')

        for team, count in sorted(

            self.finalists.items(),

            key=lambda x: x[1],

            reverse=True
        ):

            probability = (
                count
                /
                simulations
            ) * 100

            print(

                f'{team}: '
                f'{probability:.2f}%'
            )

        print(
            '\n--- Group Qualification ---'
        )

        for team, count in sorted(

            self.group_qualifications.items(),

            key=lambda x: x[1],

            reverse=True
        ):

            probability = (
                count
                /
                simulations
            ) * 100

            print(

                f'{team}: '
                f'{probability:.2f}%'
            )
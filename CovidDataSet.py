from csv import DictReader


months = {'2020-03': {'Deaths': 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0},
          '2020-04': {"Deaths": 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0},
          '2020-05': {"Deaths": 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0},
          '2020-06': {"Deaths": 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0},
          '2020-07': {"Deaths": 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0},
          '2020-08': {"Deaths": 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0},
          '2020-09': {"Deaths": 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0},
          '2020-10': {"Deaths": 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0},
          '2020-11': {"Deaths": 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0},
          '2020-12': {"Deaths": 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0},
          '2021-01': {"Deaths": 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0},
          '2021-02': {"Deaths": 0, "Pos_Result": 0, "Neg_Result": 0, "Ratio_Pos/Neg": 0.0, "Ratio_Death/Pos": 0.0}}


def fill_dict(month):
    with open("pennsylvania-history.csv", mode='r') as covid_file:
        dreader = DictReader(covid_file)
        for record in dreader:
            month_split = record['date'][0:7]
            if month_split == month:
                total_deaths = int(record['deathIncrease'])
                months[month]['Deaths'] += total_deaths
                total_pos = int(record['positiveIncrease'])
                months[month]['Pos_Result'] += total_pos
                total_neg = int(record['negativeIncrease'])
                months[month]['Neg_Result'] += total_neg
    neg_pos_round = (months[month]['Pos_Result'] / months[month]['Neg_Result'] * 100)
    add_percent = "%" + str(round(neg_pos_round, 2))
    months[month]['Ratio_Pos/Neg'] = add_percent
    death_pos_round = (months[month]['Deaths'] / months[month]['Pos_Result'] * 100)
    add_percent = "%" + str(round(death_pos_round, 2))
    months[month]['Ratio_Death/Pos'] = add_percent

    return months[month]


def total():
    total_data = {'Deaths': 0, 'Positive': 0, 'Negative': 0, 'Pos/Neg Ratio': 0.0, 'Death/Pos Ration': 0.0}
    with open("pennsylvania-history.csv", mode='r') as covid_file:
        dreader = DictReader(covid_file)
        for record in dreader:
            if record['date'] == '2021-02-17':
                total_data['Deaths'] = int(record['death'])
                total_data['Positive'] = int(record['positive'])
                total_data['Negative'] = int(record['negative'])
                neg_pos_round = (total_data['Positive'] / total_data['Negative'] * 100)
                add_percent = "%" + str(round(neg_pos_round, 2))
                total_data['Pos/Neg Ratio'] = add_percent
                death_pos_round = (total_data['Deaths'] / total_data['Positive'] * 100)
                add_percent = "%" + str(round(death_pos_round, 2))
                total_data['Death/Pos Ration'] = add_percent

    return total_data


def main():
    print("{:10} {:10} {:10} {:<10} {:15} {:10}".format('Date', 'Deaths', 'Positive', 'Negative', 'Pos/Neg Ratio', 'Death/Pos Ratio'))
    for key, values in months.items():
        fill_dict(key)
        row = "{:10} {:<10} {:<10} {:<10} {:<15} {:10}".format(key,
         values['Deaths'],
         values['Pos_Result'],
         values['Neg_Result'],
         values['Ratio_Pos/Neg'],
         values['Ratio_Death/Pos'])
        print(row)
    print("-----------------------------------------------------------------")
    total_sum = total()
    print("{:10} {:<10} {:<10} {:<10} {:<15} {:10}".format("Total: ", total_sum['Deaths'],
        total_sum["Positive"], total_sum['Negative'],
        total_sum['Pos/Neg Ratio'], total_sum['Death/Pos Ration']))


if __name__ == '__main__':
    main()
import csv

def load_file(file):
    results = []
    with open('BD_FILES/exam_results.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            results.append(row)
  
    return results

def rec_report(list):

        with open('Report.csv', 'w', newline='') as csvfile:
            fieldnames = ['Exam', 'Number of Candidates', 'Number of Passed Exams', 'Number of Failed Exams', 'Best Score', 'Worst Score']        
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in list:
                writer.writerow(row)

def analize():


    rows = load_file('BD_FILES/exam_results.csv')
    candidates_math = 0
    candidates_physics = 0
    candidates_biology = 0
    candidates_math_list = []
    candidates_physics_list = []
    candidates_biology_list = []
     

    passed_math = 0
    failed_math = 0
    failed_physics = 0
    passed_physics = 0
    passed_biology = 0
    failed_biology = 0

    best_score_math = 0
    worst_score_math = 0

    best_score_physics = 0
    worst_score_physics = 0

    best_score_biology = 0
    worst_score_biology = 0


    for row in rows:

                
        match (row['Exam Name']):

            case 'Maths':
                
                if not row['Candidate ID'] in candidates_math_list:
                    candidates_math+=1
                    candidates_math_list.append(row['Candidate ID'])
                        
                if row['Grade'] == 'Pass':
                    passed_math+=1
                else:
                    failed_math+=1

                if int(row['Score']) > best_score_math:
                    best_score_math = int(row['Score'])
                if worst_score_math > int(row['Score']) or worst_score_math == 0:
                    worst_score_math = int(row['Score'])
                

            case 'Physics':
                if not row['Candidate ID'] in candidates_physics_list:
                    candidates_physics+=1
                    candidates_physics_list.append(row['Candidate ID'])

                if row['Grade'] == 'Pass':
                    passed_physics+=1
                else:
                    failed_physics+=1

                if int(row['Score']) > best_score_physics:
                    best_score_physics = int(row['Score'])
                if worst_score_physics > int(row['Score']) or worst_score_physics == 0:
                    worst_score_physics = int(row['Score'])
                    print(worst_score_physics)
                
            
            case 'Biology':
                if not row['Candidate ID'] in candidates_biology_list:
                    candidates_biology+=1
                    candidates_biology_list.append(row['Candidate ID'])

                if row['Grade'] == 'Pass':
                    passed_biology+=1
                else:
                    failed_biology+=1

                if int(row['Score']) > best_score_biology:
                    best_score_biology = int(row['Score'])
                if worst_score_biology > int(row['Score']) or worst_score_biology == 0:
                    worst_score_biology = int(row['Score'])

    list = []            
    list.append({'Exam':'Math', 'Number of Candidates':candidates_math, 'Number of Passed Exams':passed_math, 'Number of Failed Exams':failed_math, 'Best Score':best_score_math, 'Worst Score':worst_score_math})
    list.append({'Exam':'Physics', 'Number of Candidates':candidates_physics, 'Number of Passed Exams':passed_physics, 'Number of Failed Exams':failed_physics, 'Best Score':best_score_physics, 'Worst Score':worst_score_physics})
    list.append({'Exam':'Biology', 'Number of Candidates':candidates_biology, 'Number of Passed Exams':passed_biology, 'Number of Failed Exams':failed_biology, 'Best Score':best_score_biology, 'Worst Score':worst_score_biology})
   
    rec_report(list)              

analize()




        



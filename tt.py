daysList=list(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
import csv
import random

class Subject:
    def __init__(self,name,credits,teachers,year):
        self.credits=credits
        self.name=name
        self.teachers=teachers
        self.year=year

class Lecture:
    def __init__(self,type):
        self.venue=None
        self.subject=None
        self.teacher=None
        self.type=type
    def schedule(self,venue,subject):
        if (self.subject==None):
            self.subject=subject
            return 0
    def assignTeacher(self, teacher:str):
        self.teacher=teacher
        return 1

class Timetable:
    def __init__(self):
        self.AdjMat={
            'Monday':[],
            'Tuesday':[],
            'Wednesday':[],
            'Thursday':[],
            'Friday':[]
        }

class Classroom:
    def __init__(self):
        self.tt=Timetable()
        for day in self.tt.AdjMat.keys():
            for i in range (7):
                self.tt.AdjMat[day].append(0)
    def scheduleAt(self, day, time):
        self.tt.AdjMat[day][time]=1
    def getNextFree(self, day, time):
        daysList=list(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        i=daysList.index(day)
        availableTime=time
        for k in range(i, 5):
            while self.tt[daysList[i]][availableTime] == 0:
                return (day, availableTime)
            
        return (-1, -1)



class SY_DIV1:
    def __init__(self):
        self.tt=Timetable()
        self.classroom=Classroom()
        for day in self.tt.AdjMat.keys():
            self.tt.AdjMat[day].append(Lecture(0))  # 0:lecture   1:Lab   2:Break
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(1))
            self.tt.AdjMat[day].append(Lecture(2))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
    
    def check(self,subject,day):
        for i in range(0,len(self.tt.AdjMat[day])):
            if subject==self.tt.AdjMat[day][i].subject:
                return 0
        return 1

    def assign_venue(self,venue,day,time):
        self.tt.AdjMat[day][time].venue=venue
    
    def RandomiseTT(self, subjectList, type):
        for subject in subjectList:
            i=0
            while i<subject.credits:
                day=random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
                j=0
                while j<7:
                    if self.tt.AdjMat[day][j].subject==None and self.tt.AdjMat[day][j].type==type:
                        self.tt.AdjMat[day][j].subject=subject
                        self.classroom.tt.AdjMat[day][j]=1
                        i+=1
                        break
                    j+=1
    
    def generate_data(self):
        data = []
        for i in range(5):
            startTime=9
            for j in range(7):
                temp = {}
                temp["day"] = daysList[i]
                temp["start_time"] = startTime
                if self.tt.AdjMat[daysList[i]][j].type == 0 or self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["end_time"] = startTime+1
                    startTime += 1
                elif self.tt.AdjMat[daysList[i]][j].type == 1:
                    temp["end_time"] = startTime + 1
                    temp['subject'] = f"{self.tt.AdjMat[daysList[i]][j].subject}-Lab"
                    temp['venue']=self.tt.AdjMat[daysList[i]][j].venue
                    data.append(temp)
                    startTime+=1
                    temp["end_time"]=startTime + 1
                if self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["subject"] = "Lunch Break"
                if self.tt.AdjMat[daysList[i]][j].subject:
                    temp["subject"] = self.tt.AdjMat[daysList[i]][j].subject.name
                temp["venue"] = self.tt.AdjMat[daysList[i]][j].venue
                temp['teacher']=self.tt.AdjMat[daysList[i]][j].teacher
                data.append(temp)
        return data

class SY_DIV2:
    def __init__(self):
        self.tt=Timetable()
        self.classroom=Classroom()
        for day in self.tt.AdjMat.keys():
            self.tt.AdjMat[day].append(Lecture(1))  # 0:lecture   1:Lab   2:Break
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(2))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(3))
    
    def check(self,subject,day):
        for i in range(0,len(self.tt.AdjMat[day])):
            if subject==self.tt.AdjMat[day][i].subject:
                return 0
        return 1
    
    def assign_venue(self,venue,day,time):
        self.tt.AdjMat[day][time].venue=venue
    
    def RandomiseTT(self, subjectList, type):
        for subject in subjectList:
            i=0
            while i<subject.credits:
                day=random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
                j=0
                while j<7:
                    if self.tt.AdjMat[day][j].subject==None and self.tt.AdjMat[day][j].type==type:
                        self.tt.AdjMat[day][j].subject=subject
                        self.classroom.tt.AdjMat[day][j]=1
                        i+=1
                        break
                    j+=1
    
    def generate_data(self):
        data = []
        for i in range(5):
            startTime=9
            for j in range(7):
                temp = {}
                temp["day"] = daysList[i]
                temp["start_time"] = startTime
                if self.tt.AdjMat[daysList[i]][j].type != 1:
                    temp["end_time"] = startTime + 1
                    startTime += 1
                elif self.tt.AdjMat[daysList[i]][j].type == 1:
                    temp["end_time"] = startTime + 1
                    temp['subject'] = f"{self.tt.AdjMat[daysList[i]][j].subject}-Lab"
                    temp['venue']=self.tt.AdjMat[daysList[i]][j].venue
                    data.append(temp)
                    startTime+=1
                    temp["end_time"]=startTime + 1
                if self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["subject"] = "Lunch Break"
                if self.tt.AdjMat[daysList[i]][j].subject:
                    temp["subject"] = self.tt.AdjMat[daysList[i]][j].subject.name
                temp["venue"] = self.tt.AdjMat[daysList[i]][j].venue
                temp['teacher']=self.tt.AdjMat[daysList[i]][j].teacher
                data.append(temp)
        return data

class TY_DIV1:
    def __init__(self):
        self.tt=Timetable()
        self.classroom=Classroom()
        for day in self.tt.AdjMat.keys():
            self.tt.AdjMat[day].append(Lecture(0))  # 0:lecture   1:Lab   2:Break 3:honors 4:electives
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(4))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(2))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(1))
            self.tt.AdjMat[day].append(Lecture(3))
    
    def check(self,subject,day):
        for i in range(0,len(self.tt.AdjMat[day])):
            if subject==self.tt.AdjMat[day][i].subject:
                return 0
        return 1

    def assign_venue(self,venue,day,time):
        if not self.tt.AdjMat[day][time].type:
            self.tt.AdjMat[day][time].venue=venue
    
    def RandomiseTT(self, subjectList, type):
        for subject in subjectList:
            i=0
            while i<subject.credits:
                day=random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
                j=0
                while j<7:
                    if self.tt.AdjMat[day][j].subject==None and self.tt.AdjMat[day][j].type==type:
                        self.tt.AdjMat[day][j].subject=subject
                        self.classroom.tt.AdjMat[day][j]=1
                        i+=1
                        break
                    j+=1

    def RandomiseTT_electives(self,subject,type):
        for i in range(3):
            self.tt.AdjMat[daysList[i]][2].subject=subject[0]
    
    def generate_data(self):
        data = []
        for i in range(5):
            startTime=9
            for j in range(7):
                temp = {}
                temp["day"] = daysList[i]
                temp["start_time"] = startTime
                if self.tt.AdjMat[daysList[i]][j].type != 1:
                    temp["end_time"] = startTime + 1
                    startTime += 1
                elif self.tt.AdjMat[daysList[i]][j].type == 1:
                    temp["end_time"] = startTime + 1
                    temp['subject'] = f"{self.tt.AdjMat[daysList[i]][j].subject}-Lab"
                    temp['venue']=self.tt.AdjMat[daysList[i]][j].venue
                    data.append(temp)
                    startTime+=1
                    temp["end_time"]=startTime + 1
                if self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["subject"] = "Lunch Break"
                if self.tt.AdjMat[daysList[i]][j].subject:
                    temp["subject"] = self.tt.AdjMat[daysList[i]][j].subject.name
                temp["venue"] = self.tt.AdjMat[daysList[i]][j].venue
                temp['teacher']=self.tt.AdjMat[daysList[i]][j].teacher
                data.append(temp)
            if i>=3:
                temp={}
                temp["day"]=daysList[i]
                temp["start_time"]=17
                temp["end_time"]=18
                temp["subject"]="Honors"
                data.append(temp)
        return data

class TY_DIV2:
    def __init__(self):
        self.tt=Timetable()
        self.classroom=Classroom()
        for day in self.tt.AdjMat.keys():
            self.tt.AdjMat[day].append(Lecture(0))  # 0:lecture   1:Lab   2:Break  3:honors 4: electives
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(4))
            self.tt.AdjMat[day].append(Lecture(2))
            self.tt.AdjMat[day].append(Lecture(1))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(0))
            self.tt.AdjMat[day].append(Lecture(3))

    
    def check(self,subject,day):
        for i in range(0,len(self.tt.AdjMat[day])):
            if subject==self.tt.AdjMat[day][i].subject:
                return 0
        return 1

    def assign_venue(self,venue,day,time):
        if not self.tt.AdjMat[day][time].type:
            self.tt.AdjMat[day][time].venue=venue
    
    def RandomiseTT(self, subjectList, type):
        for subject in subjectList:
            i=0
            while i<subject.credits:
                day=random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
                j=0
                while j<7:
                    if self.tt.AdjMat[day][j].subject==None and self.tt.AdjMat[day][j].type==type:
                        self.tt.AdjMat[day][j].subject=subject
                        self.classroom.tt.AdjMat[day][j]=1
                        i+=1
                        break
                    j+=1
    
    def RandomiseTT_electives(self,subject,type):
        for i in range(3):
            self.tt.AdjMat[daysList[i]][2].subject=subject[0]

    
    def generate_data(self):
        data = []
        for i in range(5):
            startTime=9
            for j in range(7):
                temp = {}
                temp["day"] = daysList[i]
                temp["start_time"] = startTime
                if self.tt.AdjMat[daysList[i]][j].type != 1:
                    temp["end_time"] = startTime + 1
                    startTime += 1
                elif self.tt.AdjMat[daysList[i]][j].type == 1:
                    temp["end_time"] = startTime + 1
                    temp['subject'] = f"{self.tt.AdjMat[daysList[i]][j].subject}-Lab"
                    temp['venue']=self.tt.AdjMat[daysList[i]][j].venue
                    data.append(temp)
                    startTime+=1
                    temp["end_time"]=startTime + 1
                if self.tt.AdjMat[daysList[i]][j].type == 2:
                    temp["subject"] = "Lunch Break"
                if self.tt.AdjMat[daysList[i]][j].subject:
                    temp["subject"] = self.tt.AdjMat[daysList[i]][j].subject.name
                temp["venue"] = self.tt.AdjMat[daysList[i]][j].venue
                temp['teacher']=self.tt.AdjMat[daysList[i]][j].teacher
                data.append(temp)
            if i>=3:
                temp={}
                temp["day"]=daysList[i]
                temp["start_time"]=17
                temp["end_time"]=18
                temp["subject"]="Honors"
                data.append(temp)
        
        return data


def SY_COMP(div1,div2):
    for i in range(5):
        for j in range(7):
            if div1.classroom.tt.AdjMat[daysList[i]][j] and div2.classroom.tt.AdjMat[daysList[i]][j]:
                div1.assign_venue(203,daysList[i],j)
                div2.assign_venue(201,daysList[i],j)
            elif div1.classroom.tt.AdjMat[daysList[i]][j]:
                div1.assign_venue(203,daysList[i],j)
            elif div2.classroom.tt.AdjMat[daysList[i]][j]:
                div2.assign_venue(203,daysList[i],j)

    for i in range(5):
        for j in range(7):
            if div1.tt.AdjMat[daysList[i]][j].subject and div2.tt.AdjMat[daysList[i]][j].subject and div1.tt.AdjMat[daysList[i]][j].subject.name==div2.tt.AdjMat[daysList[i]][j].subject.name:
                if len(div1.tt.AdjMat[daysList[i]][j].subject.teachers)==1:
                    div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    for m in div2.tt.AdjMat[daysList[i]]:
                        if m.subject != div2.tt.AdjMat[daysList[i]][j].subject:
                            m.subject, div2.tt.AdjMat[daysList[i]][j].subject=div2.tt.AdjMat[daysList[i]][j].subject, m.subject
                            break
                        m.assignTeacher(m.subject.teachers[0])
                else:
                    div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[1])
            else:
                if div1.tt.AdjMat[daysList[i]][j].subject and div2.tt.AdjMat[daysList[i]][j].subject:
                    div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    if len(div2.tt.AdjMat[daysList[i]][j].subject.teachers)>1:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[1])
                    else:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                elif div1.tt.AdjMat[daysList[i]][j].subject:
                    div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                elif div2.tt.AdjMat[daysList[i]][j].subject:
                    if len(div2.tt.AdjMat[daysList[i]][j].subject.teachers)>1:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[1])
                    else:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[0])


def TY_COMP(div1,div2):
    for i in range(5):
        for j in range(7):
            if j==2 and i<=2:
                div1.assign_venue(202,daysList[i],j)
                div2.assign_venue(204,daysList[i],j)
                continue
            if div1.classroom.tt.AdjMat[daysList[i]][j] and div2.classroom.tt.AdjMat[daysList[i]][j]:
                div1.assign_venue(202,daysList[i],j)
                div2.assign_venue(204,daysList[i],j)
            elif div1.classroom.tt.AdjMat[daysList[i]][j]:
                div1.assign_venue(202,daysList[i],j)
            elif div2.classroom.tt.AdjMat[daysList[i]][j]:
                div2.assign_venue(204,daysList[i],j)

    for i in range(5):
        for j in range(7):
            if div1.tt.AdjMat[daysList[i]][j].subject and div2.tt.AdjMat[daysList[i]][j].subject and div1.tt.AdjMat[daysList[i]][j].subject.name==div2.tt.AdjMat[daysList[i]][j].subject.name:
                if len(div1.tt.AdjMat[daysList[i]][j].subject.teachers)==1:
                    div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    for m in div2.tt.AdjMat[daysList[i]]:
                        if m.subject != div2.tt.AdjMat[daysList[i]][j].subject:
                            m.subject, div2.tt.AdjMat[daysList[i]][j].subject=div2.tt.AdjMat[daysList[i]][j].subject, m.subject
                            break
                        m.assignTeacher(m.subject.teachers[0])
                elif len(div1.tt.AdjMat[daysList[i]][j].subject.teachers)>1:
                    div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[1])
            else:
                if div1.tt.AdjMat[daysList[i]][j].subject and div2.tt.AdjMat[daysList[i]][j].subject:
                    div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                    if len(div2.tt.AdjMat[daysList[i]][j].subject.teachers)>1:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[1])
                    else:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                elif div1.tt.AdjMat[daysList[i]][j].subject:
                    div1.tt.AdjMat[daysList[i]][j].assignTeacher(div1.tt.AdjMat[daysList[i]][j].subject.teachers[0])
                elif div2.tt.AdjMat[daysList[i]][j].subject:
                    if len(div2.tt.AdjMat[daysList[i]][j].subject.teachers)>1:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[1])
                    else:
                        div2.tt.AdjMat[daysList[i]][j].assignTeacher(div2.tt.AdjMat[daysList[i]][j].subject.teachers[0])


def write_to_csv(filename, data):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['day', 'start_time', 'end_time', 'subject', 'venue','teacher']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

27-02-2023 OpenSystems Universitat de Barcelona, opensystems@ub.edu ; Franziska Peter, fpeter@ub.edu

GENERAL INFORMATION
------------------

Dataset title:

	    Data from: CoAct Citizen Science chatbot explores social support networks in mental health based on lived experiences

Authorship:

	    Franziska Peter
	    Universitat de Barcelona
	    ORCID: 0000-0003-0916-8056
	    
        Isabelle Bonhoure
	    Universitat de Barcelona
	    ORCID: 0000-0002-2971-3069
	    
	    Anna Cigarini
	    Universitat de Barcelona
	    ORCID: 0000-0002-9328-8589

        Perelló, Josep
        Universitat de Barcelona
        ORCID: 0000-0001-8533-6539



DESCRIPTION
----------

A data set on lived experiences in the context of social support in mental health, created within a Citizen Social Science project. 

Societies around the world increasingly encounter wicked and complex problems, such as those related to mental health, environmental justice, and youth employment. **CoAct as a EU-funded global effort** addresses these problems by deploying Citizen Social Science. 

**Citizen Social Science** is understood here as participatory research co-designed and directly driven by citizen groups sharing a social concern. This methodology wants to give citizen groups an equal ‘seat at the table’ through **active participation in research**, from the design to the interpretation of the results and their transformation into concrete actions. Citizens thus act as **co-researchers** and are recognised as in-the-field competent experts. 

In Barcelona, a group of **32 co-researchers** work together with the OpenSystems group, Universitat de Barcelona, the Catalan Federation of Mental Health (Federació Salut Mental Catalunya), and with the help of many others on a better understanding of informal **social support networks in mental health** in the project <b><i>CoActuem per la Salut Mental</i></b> (lit. “We act together for mental health”). The co-researchers, who are either persons with a personal history of mental health problems or are family members of the latter, contributed their **personal experiences related to social support** in the form of **222 micro-stories**, each shorter than 400 characters, and most accompanied by an illustration by Pau Badia.

Those micro-stories form the heart of the first co-created Citizen Science chatbot, the code of which is open on https://github.com/Chaotique/CoActuem_per_la_Salut_Mental_Chatbot.git . The **Telegram chatbot** sends them to participants **on a daily basis over the course of a year** and asks them either, whether they and/ or their close surrounding lived this experience, too (stories of type C), or, how they would or would have reacted in the presented situation (stories of type T). The answers of each participant can be contrasted with the individual participants’ answer to a 32-questions **socio-demographic survey**. Further, the timing of the messages is included to allow for a broader analysis.  

The chatbot is still running, hence this data set will still be updated. For further information on the project **CoAct**, see https://coactproject.eu/. For further details on the co-creation process and purpose of the chatbot **CoActuem per la Salut Mental**, take a look on https://coactuem.ub.edu/. Please direct your questions regarding the data set to **coactuem[at]ub.edu**.

ACKNOWLEDGEMENTS
----------
The CoAct project has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement number 873048. We especially thank the co-researchers for the passion and time invested.

KEYWORDS
----------
Citizen Science, Citizen Social Science, Co-creation, Public Participation, Catalonia, Mental Health, Social Support, Chatbot


ACCESS INFORMATION
------------------------

**LICENSE:** Dataset under Attribution-NonCommercial-ShareAlike 4.0 International; legal text available at https://creativecommons.org/licenses/by-nc-sa/4.0/

**Dataset DOI:** 10.5281/zenodo.7443141


FILE DESCRIPTION
------------------------

This data set is a result of the Citizen Social Science project "CoActuem per la Salut" (https://coactuem.ub.edu), funded within the CoAct project that has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement number 873048 (https://coactproject.eu/). The project seeks a better understanding of informal social support networks in mental health.

For the data collection, lived experiences related to the topic of support in mental health are shared via a Telegram chatbot the code of which is public under https://github.com/Chaotique/CoActuem_per_la_Salut_Mental_Chatbot. The experiences are bundled in short micro-stories which participants receive on a daily basis and to which they can react by pressing buttons. For an explanation of the technical setup of the chatbot consult chapter 4. of [https://zenodo.org/record/6078916](https://zenodo.org/record/6078916).

The data collection is still running. The data presented in this version v0 was collected between 09.07.2021 and 26.02.2023; the bot was officially launched on 27.11.2021. From all 1222 participants who accessed the chatbot so far, this data set comprises only those 748 who gave their Informed Consent (see https://zenodo.org/record/5806065, p. 21-38). Each participant is represented with a unique identifier, e.g. 518e9b8, which is the same across all data set files. 

The data set comprises:
Answers to the micro-stories' questions, answers to the socio-demographic survey, the relative timings of receiving the questions and answering, sample micro-stories, the welcome dialogue, capacitation dialogue, and socio-demographic survey messages and questions in English.

The answers and timings are both available as .csv and .pkl (pickle) files. While both filetypes contain the same information, the pickle files allow for an easy loading into one python pandas MultiIndex DataFrame.

The data set contains the following folders and files (for the plain folder structure, see [files_overview.md](./files_overview.md)):

## Microstories_and_entry_dialogues/ 

The micro stories and dialogues are presented in both PDF and JSON format. While the .json files reveal all detail on the technical structure of the dialogues, including all identifiers, the .pdf files are simplyfied to the main messages, images, and emojis as send to the participants via the chatbot. To understand the structure of the .json files, please consult the appendix of [https://zenodo.org/record/6078916](https://zenodo.org/record/6078916).

The dialogues sent to the participants are either so-called micro-stories that pose a situation or dilemma and ask the participant for a reaction, or a sociodemographic survey, or otherwise dialogues that inform the participants on the context of the citizen science research, etc. The main scientific interest lies in the particpants' answers to the sociodemographic survey and to the micro-stories.

There are 130 micro-stories that present a situation related to social support in mental health and ask the two questions *What about you? Have you had the same experience?* and *And those around you... Has anybody had the same experience?* with respective rating scales A) to C) (see [Example_stories_of_type_C_en.pdf](./Microstories_and_entry_dialogues/Example_stories_of_type_C_en.pdf)), called stories of type C.

There are another 56 micro-stories that pose questions like *What would you do?*, *What do you do?*, or *What would you have done?* in the presented situation. These latter stories of type T offer two to four answering options that are paired to 92 dialogues with binary option A) or B) (see [Example_stories_of_type_T_en.pdf](./Microstories_and_entry_dialogues/Example_stories_of_type_T_en.pdf)). 

Note that the answer options A), B), and C) are presented to the participants as buttons. For stories C and T, not more than two examples are given as PDF and JSON file are released so far, as the chatbot is still running. The full set of stories in all four languages English, Spanish, Catalan, and German will be published on a different domain.

## <a name="Answers_MS">Answers_to_Microstories/</a>

The folder contains the participants' answers to the micro-stories (in two pickle files or two folders with csv files, respectively) as well as a file with the order in which they are sent to the chatbot participants. 

The 130 micro-stories of type C and ask the two questions *What about you? Have you had the same experience?* (indexed with "yo") and *And those around you... Has anybody had the same experience?* (indexed with "otro").

The answers of the 56 situations and dilemmas of type T with questions like *What would you do?*, *What do you do?*, or *What would you have done?* offer two to four answering options that are paired to form 92 micro-stories with binary option the answer of which is saved in variable "x". 

For both story types, and thus for the three questions, the participants can revise their answer twice. The first answer they give are stored in a column with suffix *_1*; in case they change their mind the second answer is stored with suffix *_2*, and in some cases even a third answer is stored with suffix *_3*. The respective definitive answer of each participant to the respective story is stored in a respective additional column with suffix *_final*. 

Entirely empty columns are excluded in order to stay under the Excel limit of 1024 columns.

### answers_stories_C.pkl and stories_type_C/

Answers to stories of type C. For the exact phrasing of the two questions and the respective answering options, see file [Example_stories_of_type_C_en.pdf](./Microstories_and_entry_dialogues/Example_stories_of_type_C_en.pdf). The complete set of stories will be published after the termination of the chatbot run.

Load in python as MultiIndex pandas DataFrame: 

        import pandas as pd
        df_C = pd.read_pickle("./Answers_to_Microstories/answers_stories_C.pkl")

Load in R, story by story, for instance as: 

        answers_C <- read.csv("./Answers_to_Microstories/stories_type_C/answers_Obrir_camí.csv")


### answers_stories_T.pkl and stories_type_T/

Answers to stories of type T. To know which story combines which pair of answering option, see file **Table_answers_stories_T.csv**. The complete set of stories will be published after the termination of the chatbot run.

Load in python as MultiIndex pandas DataFrame: 

        import pandas as pd
        df_T = pd.read_pickle("./Answers_to_Microstories/answers_stories_T.pkl")

Load in R, story by story, for instance as: 

        answers_T <- read.csv("./Answers_to_Microstories/stories_type_T/answers_Incomprensió_22.csv")

Micro-stories of type T have n = 2 ... 4 answer options, represented by lowercase letters a-d, and result in n*(n-1)/2 stories with pair-wise combinations of these answers. The pairing is documented in file [Table_answers_stories_T.csv](./Microstories_and_entry_dialogues/Table_answers_stories_T.csv). As a result, chatbot participants always choose between only two options. 

### order_of_stories_as_sent_via_chatbot.csv

The participants receive the stories and dialogues in a fixed order, starting with a welcome dialogue in which they can give their informed consent. In a capacitation dialogue that follows right after, they get to know the two types of stories, C and T, and the general functioning of the chatbot. 

The sociodemographic survey, consisting of 32 questions, follows without any pause. After that, participants receive one story per day, and here and there short informative dialogues on the project and research (for details on the dialogues, see file [other_dialogues.pdf](./Microstories_and_entry_dialogues/other_dialogues.pdf). 

Additionally to the dialogues listed in this file, they can call dialogues to adapt the language, time zone, and frequency of stories, or to pause and resume the chatbot interaction.

## Sociodemographic_survey/ 

Answers to the sociodemographic survey that is presented to the chatbot participants as the third dialoge, see [meta_data_answers.pdf](./Sociodemographic_survey/meta_data_answers.pdf) for a comprehensive overview over the presented columns, and see [other_dialogues.pdf](./Microstories_and_entry_dialogues/other_dialogues.pdf) and [sociodem_coact.json](./Microstories_and_entry_dialogues/sociodem_coact.json) for all detail. Again, both, pickle and csv file with the answers are included, and can be loaded just as described above for files in folder [Answers_to_Microstories/](#Answers_MS). 

## Timing_of_answers/

Files [answer_times_pickle_diff_to_cont_C.pkl](./answer_times_pickle_diff_to_cont_C.pkl/answer_times_pickle_diff_to_cont_C.pkl) and [answer_times_pickle_diff_to_cont_T.pkl](./answer_times_pickle_diff_to_cont_T.pkl/answer_times_pickle_diff_to_cont_T.pkl) and csv files in folders [timing_of_stories_type_C/](./Timing_of_answers/timing_of_stories_type_C/) and [timing_of_stories_type_T/](./Timing_of_answers/timing_of_stories_type_T/) contain the timings of participant-chatbot interactions (the same data in pickle and csv format, respectively), relative to the timing of the first interaction from bot to participant per micro-story (*diff_to_cont* meaning difference to first continue button). 
In stories C and T, this is the first "Continue" button in the story that participants click, respectively, see e.g. line 9 page 6 in [other_dialogues.pdf](./Microstories_and_entry_dialogues/other_dialogues.pdf). Files from_or_to_bot* indicate whether the timing was recorded in the moment when the chatbot sent, or when it received a query, respectively. More detail can be obtained by matching the identifiers, i.e. the column names, with the respective vars values in the .json files in [Microstories_and_entry_dialogues/](.Microstories_and_entry_dialogues/). Especially the timings of when the bot sent queries are not available for all stories and participants, as they were recorded only from 28th Sept 2021 on, and before that they are listed as "unknown". The participants identifiers correspond to those in the micro-stories results and sociodemographic survey.



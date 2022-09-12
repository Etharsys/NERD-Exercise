/*------------------------------------------------------------------------*
 Project: Support Recruitment Test

 Copyright (C) 2022 Nintendo, All rights reserved.

 These coded instructions, statements, and computer programs contain proprietary
 information of Nintendo and/or its licensed developers and are protected by
 national and international copyright laws. They may not be disclosed to third
 parties or copied or duplicated in any form, in whole or in part, without the
 prior written consent of Nintendo.

 The content herein is highly confidential and should be handled accordingly.
*------------------------------------------------------------------------*/
pipeline 
{
    agent any
        
    stages
    {

        stage ('Build')
        {
            steps
            {
                echo 'Building native app...'

                sh '''rm -Rf native/build'''
                sh '''mkdir native/build'''
                dir ('native/build') 
                {
                    sh '''cmake ..'''
                    sh '''make'''
                }

                echo 'Native app builded'
            }
        }

        stage ('Test')
        {
            steps 
            {         
                echo 'Testing python3 app...'

                sh '''python3 run_tests.py'''

                echo 'Python app tests passed'
                echo 'Testing native app...'

                sh '''native/build/NERD-test'''
                
                echo 'Native app tests passed'
            }
        }

    }
}
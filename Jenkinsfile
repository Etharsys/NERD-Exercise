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

        stage ('Linux build')
        {
            steps
            {
                echo 'Building app [Linux]...'
                // sh '''python3 unstable_app.py'''
                sh '''cmake unstable_app_repo/native'''
                echo 'App builded [Linux]'
            }
        }

        stage ('Linux test')
        {
            steps 
            {         
                echo 'Testing app [Linux]...'
                sh '''python3 run_tests.py'''
                sh '''ls unstable_app_repo/native'''
                echo 'All tests passed [Linux]'
            }
        }

        stage('Linux clean')
        {
            steps
            {
                echo 'Removing build native application'
                sh '''rm -R unstable_app_repo/native/build'''
            }
        }

    }
}
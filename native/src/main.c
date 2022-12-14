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
#include <stdio.h>

#include "nerd/platform.h"

int main(int argc, char **argv)
{
    printf("Hello Support from %s\n", get_platform_name());
    return 0;
}
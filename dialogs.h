// INCLUDE FILE generated by "Pelles C for Windows, version 8.00".

#ifndef _DIALOGS_H
#define _DIALOGS_H

#ifdef _DIALOGS_
#define DIALOGSAPI  __declspec(dllexport)
#else
#define DIALOGSAPI  __declspec(dllimport)
#endif /* _DIALOGS_ */

#ifndef WINAPI
#define WINAPI  __stdcall
#endif

DIALOGSAPI int WINAPI MsgBox(char*,char*);
DIALOGSAPI char* WINAPI InputBox(char*,char*);
DIALOGSAPI char* WINAPI OpenDialog();
DIALOGSAPI char* WINAPI SaveDialog();
#endif /* _DIALOGS_H */
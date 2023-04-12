using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RunPython : MonoBehaviour
{
    public string pythonFileName;
    public string nose;
    public string body;
    public string thruster;
    public void python()
    {
        string pythonArgs = pythonFileName + " " + nose + " " + body + " " + thruster;
        System.Diagnostics.Process.Start("python", pythonArgs);
    }
}

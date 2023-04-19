using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using static System.Net.Mime.MediaTypeNames.Text;

public class yPositionDisplay : MonoBehaviour
{
    
    private float height;
    public Text heightText;

    void Update()
    {
        height = Movement.yPos[Movement.curI];
        if (height < 0.1)
        {
            height = 0;
        }
        heightText.text = "Y-Position: " + height.ToString();
    }

}

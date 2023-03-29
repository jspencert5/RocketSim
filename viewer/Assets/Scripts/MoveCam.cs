using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveCam : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (isMoving.isMovin)
        {
            if (Movement.i < Movement.yPos.Length)
            {
                float step = Movement.ySpeeds[Movement.i] * Time.deltaTime;

                transform.position = Vector3.MoveTowards(transform.position, new Vector3(14.99f, Movement.yPos[Movement.i], -0.27f), step);
                //transform.Translate(Vector3.right * Movement.xSpeeds[Movement.i] * Time.deltaTime);}
            }
        }
    }
}

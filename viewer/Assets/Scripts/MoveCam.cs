using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveCam : MonoBehaviour
{
<<<<<<< Updated upstream
    // Start is called before the first frame update
    void Start()
    {
        
    }
=======
    public GameObject objec;
    private Vector3 offset = new Vector3(0f, 6.11f, 14.73f);
>>>>>>> Stashed changes

    // Update is called once per frame
    void Update()
    {
<<<<<<< Updated upstream
        if (isMoving.isMovin)
        {
            if (Movement.i < Movement.yPos.Length)
            {
                float step = Movement.ySpeeds[Movement.i] * Time.deltaTime;

                transform.position = Vector3.MoveTowards(transform.position, new Vector3(14.99f, Movement.yPos[Movement.i], -0.27f), step);
                //transform.Translate(Vector3.right * Movement.xSpeeds[Movement.i] * Time.deltaTime);}
            }
        }
=======
        // Get the Transform component of the object we want to follow
        Transform targetTransform = objec.GetComponent<Transform>();

        // Calculate the desired position of the camera
        Vector3 desiredPosition = targetTransform.position + offset;

        // Set the position of the camera to the desired position
        transform.position = desiredPosition;
>>>>>>> Stashed changes
    }
}

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MouseMove : MonoBehaviour
{
    private Vector3 MouseOffset;
    private float MouseCoord;
    private void OnMouseDown()
    {
        MouseCoord = Camera.main.WorldToScreenPoint(gameObject.transform.position).z;
    }

    private Vector3 GetMousePosition()
    {
        Vector3 mousePoint = Input.mousePosition;
        mousePoint.z = MouseCoord;
        return Camera.main.ScreenToWorldPoint(mousePoint);
    }

    private void OnMouseDrag()
    {
        GetComponent<Rigidbody>().Sleep();
        transform.position = GetMousePosition() + MouseOffset;
        GetComponent<Rigidbody>().WakeUp();
    }
}


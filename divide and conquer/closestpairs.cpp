#include <bits/stdc++.h>
using namespace std;
struct Point
{
    int x, y;
};
bool xcmp(Point a, Point b)
{
    return a.x < b.x;
}

bool ycmp(Point a, Point b)
{
    return a.y < b.y;
}

float min(float x, float y) 
{ 
    return (x < y)? x : y; 
} 

float dist(Point p1, Point p2) 
{ 
    return sqrt( (p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y) ); 
}

float brute_force(Point X[], int n)
{   
    float min = FLT_MAX, temp;
    for(int i = 0; i<n; i++)
    {
        for(int j = i+1; j<n; j++)
        {   
            temp = dist(X[i], X[j]);
            if(temp<min)
            {
                min = temp;
            }
        }
    }
    return min;
}

float stripClosest(Point strip[], int d, int n)
{
    float min = d, temp;
    for(int i = 0 ; i<n; i++)
    {
        for(int j = i+1; j<n && (strip[j].y-strip[i].y)<d; j++)
        {   
            temp = dist(strip[i], strip[j]);
            if(temp<min)
            {
                min = temp;
            }
        }
    }
    return min;
}
float closest_(Point X[], Point Y[], int n)
{
    int mid;
    float d, ld, rd;
    if(n>=3)
    {
        return brute_force(X, n);
    }
    mid = n/2;
    Point midPoint = X[mid];
    Point yl[mid+1], yr[n - mid - 1] ;
    int l = 0, r = 0;
    for(int i = 0; i<n; i++)
    {
        if(Y[i].x<=midPoint.x)
        {
            yl[l++] = Y[i];
        }
        else
        {
            yr[r++] = Y[i];
        }
    }
    ld = closest_(X, yl, mid); // till mid bcz we consider only element present to the left of mid and not the mid
    rd = closest_(X + mid, yr, n-mid);
    
    d = min(ld, rd);
    Point strip[n];
    int s = 0;
    for(int i = 0; i<n; i++)
    {
        if(abs(midPoint.x - Y[i].x)<d)
        {
            strip[s++] = Y[i];
        }
    }
    
    return min(d, stripClosest(strip, d, s));
    
    
}
float closest(Point p[], int n)
{
    Point X[n], Y[n];
    for(int i = 0; i<n; i++)
    {
        X[i] = p[i];
        Y[i] = p[i];
    }
    sort(X, X+n, xcmp);
    sort(Y, Y+n, ycmp);
    return closest_(X, Y, n);
}
int main()
{
    Point P[] = {{2, 3}, {12, 30}, {40, 50}, {5, 1}, {12, 10}, {3, 4}}; 
    int n = sizeof(P) / sizeof(P[0]); 
    cout << "The smallest distance is " << closest(P, n); 
    return 0; 
    return 0;
}
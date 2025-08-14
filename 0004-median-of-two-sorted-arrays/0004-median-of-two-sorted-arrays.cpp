class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        double answer;
        int sizeNums1=nums1.size();
        int sizeNums2=nums2.size();
        vector<int> numsM;
        vector<int> numsMS;
        int sizeNumsMS;
        numsM.insert(numsM.end(),nums1.begin(),nums1.end());
numsM.insert(numsM.end(),nums2.begin(),nums2.end());
        int sizeNumsM=numsM.size();
        int temp;
        int tempi;
        int k;
        int min;
        for (int i=0;i<sizeNumsM;i++)
            {
                min=*min_element(numsM.begin(),numsM.end());
                numsMS.push_back(min);
                vector<int> :: iterator itr;
                itr = find(numsM.begin(), numsM.end(),min);
                if (itr!=numsM.end())
                {
                    tempi = distance(numsM.begin(), itr);
                }
                numsM.erase(numsM.begin()+tempi);
            }
        sizeNumsMS=numsMS.size();
        double med1;
        double med2;
        if (sizeNumsMS%2==0) //even
        {
            med1=numsMS[(sizeNumsMS)/2];
            med2=numsMS[(sizeNumsMS/2)-1];
            answer=(med1+med2)/2;
        }
        else //odd
        {
            med1=numsMS[(sizeNumsMS-1)/2];
            answer=med1;
        }
        return answer;
        
    }
};
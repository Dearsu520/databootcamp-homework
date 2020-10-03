Attribute VB_Name = "Module1"
Sub Ticker():
    For Each ws In Worksheets
        ws.Range("I1").Value = "Ticker"
        lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        SummaryRow = 2
        For i = 2 To lastrow
            If ws.Cells(i, 1).Value <> ws.Cells(i + 1, 1) Then
                ws.Cells(SummaryRow, 9).Value = ws.Cells(i, 1).Value
                SummaryRow = SummaryRow + 1
            End If
        Next i
    Next ws
End Sub
Sub YearlyandPercentageChange():
    For Each ws In Worksheets
        ws.Range("J1").Value = "Yearly Change"
        ws.Range("K1").Value = "Percent Change"
        lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        SummaryRow = 2
        Openrow = 2
        closerow = 2
        For i = 2 To lastrow
            If ws.Cells(i, 1).Value = ws.Cells(i + 1, 1) Then
                closerow = closerow + 1
            Else
                ws.Range("J" & SummaryRow).Value = ws.Range("F" & closerow).Value - ws.Range("C" & Openrow).Value
                If ws.Range("C" & Openrow).Value > 0 Then
                    ws.Range("K" & SummaryRow).Value = ws.Range("J" & SummaryRow).Value / ws.Range("C" & Openrow).Value
                Else
                    ws.Range("K" & SummaryRow).Value = "0.00%"
                End If
                Openrow = i + 1
                closerow = closerow + 1
                SummaryRow = SummaryRow + 1
            End If
        Next i
        ws.Range("K2:K" & (SummaryRow - 1)).NumberFormat = "0.00%"
    Next ws
End Sub
Sub TotalStockVolume():
    For Each ws In Worksheets
        ws.Range("L1").Value = "Total Stock Volume"
        lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
        SummaryRow = 2
        ws.Range("L" & SummaryRow).Value = ws.Range("G2").Value
        For i = 2 To lastrow
            If ws.Range("A" & i).Value = ws.Range("A" & (i + 1)) Then
                ws.Range("L" & SummaryRow).Value = ws.Range("L" & SummaryRow).Value + ws.Range("G" & (i + 1)).Value
            Else
                SummaryRow = SummaryRow + 1
                ws.Range("L" & SummaryRow).Value = ws.Range("C" & (i + 1)).Value
            End If
        Next i
    Next ws
End Sub
Sub ConditionalFormatting():
    For Each ws In Worksheets
        lastrow = ws.Cells(Rows.Count, 10).End(xlUp).Row
        For i = 2 To lastrow
            If ws.Cells(i, 10).Value > 0 Then
                ws.Cells(i, 10).Interior.Color = vbGreen
            ElseIf ws.Cells(i, 10).Value < 0 Then
                ws.Cells(i, 10).Interior.Color = vbRed
            End If
        Next i
    Next ws
End Sub
Sub Chanllenge():
    For Each ws In Worksheets
        lastrow = ws.Cells(Rows.Count, 11).End(xlUp).Row
        ws.Range("O2").Value = "Greatest % Increase"
        ws.Range("O3").Value = "Greatest % Decrease"
        ws.Range("O4").Value = "Greatest Total Volume"
        ws.Range("P1").Value = "Ticker"
        ws.Range("Q1").Value = "Value"
        MaxNumber = ws.Range("K2").Value
        MinNumber = ws.Range("K2").Value
        MaxTotalVolume = ws.Range("L2").Value
        For i = 2 To lastrow
            If ws.Range("K" & i).Value > MaxNumber Then
                MaxNumber = ws.Range("K" & i).Value
                ws.Range("Q2").Value = MaxNumber
                ws.Range("P2").Value = ws.Range("I" & i).Value
            End If
            If ws.Range("K" & i).Value < MinNumber Then
                MinNumber = ws.Range("K" & i).Value
                ws.Range("Q3").Value = MinNumber
                ws.Range("P3").Value = ws.Range("I" & i).Value
            End If
            If ws.Range("L" & i).Value > MaxTotalVolume Then
                MaxTotalVolume = ws.Range("L" & i).Value
                ws.Range("Q4").Value = MaxTotalVolume
                ws.Range("P4").Value = ws.Range("I" & i).Value
            End If
        Next i
        ws.Range("Q2:Q3").NumberFormat = "0.00%"
    Next ws
End Sub

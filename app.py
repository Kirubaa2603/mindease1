import React, { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Select, SelectTrigger, SelectContent, SelectItem } from "@/components/ui/select";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";

const motivationPrompts = [
  "You are stronger than you think! 💪", 
  "Every day is a fresh start 🌿", 
  "Believe in yourself! ✨", 
  "Challenges make you grow 🌱",
  "You have come so far, keep going! 🚀",
  "Success is built on small efforts daily! 🏆",
  "Your potential is limitless! 💡",
  "You are doing better than you think! 💕",
  "Dream big, work hard! 🔥",
  "Stay positive, better days are coming! 🌈"
];

const anxietyPrompts = [
  "Take a deep breath, inhale... exhale... 😌", 
  "Focus on what you can control 💖", 
  "You are safe and loved ❤️", 
  "Everything is temporary, this will pass 🌊",
  "Slow down and be present in the moment 🌿",
  "Ground yourself: Name 5 things you see 👀",
  "Repeat: 'I am in control of my emotions' 🧘",
  "Drink some water and relax 💧",
  "Stretch your shoulders and breathe 🤲",
  "You got this, take one step at a time 🏞️"
];

const studyTips = [
  "Use the Pomodoro technique 🍅",
  "Try the Feynman technique to understand better ✍️",
  "Teach someone else to reinforce learning 🧑‍🏫",
  "Take regular breaks to refresh your mind ☕",
  "Make mind maps to visualize concepts 🎨",
  "Summarize key points in your own words 📖",
  "Practice active recall to strengthen memory 🧠",
  "Change your study environment for freshness 🌳",
  "Use mnemonics to remember tough topics 🔤",
  "Stay hydrated and get enough sleep 🌙"
];

const selfCareTips = [
  "Stretch your body, relieve tension 🧘",
  "Hydrate! Your brain needs water 💧",
  "Take a mindful 5-minute break 🌿",
  "Rest your eyes, avoid screen fatigue 👀",
  "Go for a short walk and refresh 🚶",
  "Listen to calming music 🎶",
  "Journal your thoughts and feelings 📖",
  "Get some fresh air outside 🍃",
  "Light a candle or use aromatherapy 🕯️",
  "Celebrate small wins, you're doing great! 🎉"
];

const emotions = {
  happy: "Enjoy the moment and spread positivity! 😊",
  sad: "You're not alone, things will get better! 💙",
  stressed: "Take a deep breath, you've got this! 💪",
  tired: "Rest up, your body and mind need it! 🌙",
  anxious: "Focus on what you can control, breathe in & out! 🌿"
};

export default function MindEaseApp() {
  const [selectedEmotion, setSelectedEmotion] = useState("");
  const [emotionMessage, setEmotionMessage] = useState("");
  const [studySubjects, setStudySubjects] = useState([]);
  const [subjectCount, setSubjectCount] = useState(0);
  const [studyTime, setStudyTime] = useState("");
  const [timer, setTimer] = useState(null);

  useEffect(() => {
    if (selectedEmotion) {
      setEmotionMessage(emotions[selectedEmotion]);
    }
  }, [selectedEmotion]);

  const handleGeneratePlan = () => {
    alert("Study plan generated! 📚");
  };

  return (
    <div className="p-4 space-y-6 bg-blue-50 min-h-screen text-gray-800">
      <h1 className="text-2xl font-bold text-center">💙 Welcome to MindEase Tools 💙</h1>
      
      <Card>
        <CardContent>
          <h2 className="text-xl font-semibold">How do you feel today? 🌈</h2>
          <Select onValueChange={setSelectedEmotion}>
            <SelectTrigger>Select an emotion</SelectTrigger>
            <SelectContent>
              {Object.keys(emotions).map((emotion) => (
                <SelectItem key={emotion} value={emotion}>{emotion}</SelectItem>
              ))}
            </SelectContent>
          </Select>
          {emotionMessage && <p className="mt-2 text-lg">{emotionMessage}</p>}
        </CardContent>
      </Card>
      
      <Card>
        <CardContent>
          <h2 className="text-xl font-semibold">Study Planner Generator 📖</h2>
          <Input
            type="number"
            placeholder="Number of subjects"
            onChange={(e) => setSubjectCount(e.target.value)}
          />
          {[...Array(Number(subjectCount))].map((_, i) => (
            <div key={i} className="space-y-2">
              <Input placeholder={`Subject ${i + 1} Name`} />
              <Input type="number" placeholder="Number of Lessons" />
            </div>
          ))}
          <Input
            type="number"
            placeholder="Total study duration (in hours)"
            onChange={(e) => setStudyTime(e.target.value)}
          />
          <Button onClick={handleGeneratePlan}>Generate Study Plan</Button>
        </CardContent>
      </Card>
      
      <Card>
        <CardContent>
          <h2 className="text-xl font-semibold">Daily Affirmation 💡</h2>
          <p className="mt-2">"Every small step counts towards success! 🌟"</p>
        </CardContent>
      </Card>
      
      <Card>
        <CardContent>
          <h2 className="text-xl font-semibold">Study Timer ⏳</h2>
          <Button onClick={() => setTimer(setTimeout(() => alert("Time's up!"), studyTime * 60 * 1000))}>Start Timer</Button>
          <Button onClick={() => clearTimeout(timer)}>Stop Timer</Button>
        </CardContent>
      </Card>
    </div>
  );
}

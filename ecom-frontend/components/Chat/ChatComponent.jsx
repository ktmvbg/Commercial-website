'use client'
import React, { useRef } from "react";
import ChatHeader from "./ChatHeader/ChatHeader";
import ChatContent from "./ChatContent/ChatContent";
import ChatInputBox from "./ChatInputBox/ChatInputBox";
import { useGetMessages } from "hooks/useGetMessages";
import { ArrowPathIcon } from "@heroicons/react/24/outline";
import { messages } from "types/Message";

const Chat = () => {
   /** Simulate a hook fetching the data */
   //   const {
   //     messages: { data }
   //   } = useGetMessages();

   const data = messages;

   /** State to control new messages */
   const [chatMessages, setChatMessages] = React.useState([]);

   /**
    *
    * @param message
    * "Create" a new message
    */
   
   const sendANewMessage = (message) => {
      setChatMessages((prevMessages) => [...prevMessages, message]);
      fetch('http://127.0.0.1:8000/api/chat/openai35', {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json',
         },
         body: JSON.stringify({message: message.text}),
      })
      .then(response => {
         if(response.ok) {
            return response.json()
         } else {
            return {
               message: "Cannot send message",
               created_at: (new Date()).toISOString()
            }
         }
      })
      .then(data => {
         setChatMessages((prevMessages) => [...prevMessages, {
            text: data.response,
            sentBy: "Bot chat",
            sentAt: new Date(data.created_at),
            isChatOwner: false
         }]);
      })
   };

   /**
    * Reset chat to the default messages
    */
   const resetChat = () => {
      setChatMessages([]);
   };

   return (
      //  <div className="max-w-md mx-auto mt-32 ">
      <div className="max-w-md">
         <div className="flex flex-row justify-between items-center py-2">
            <button
               type="button"
               onClick={() => resetChat()}
               className="hover:bg-gray-100 rounded-full font-medium text-sm p-1.5 text-center inline-flex items-center"
            >
               <ArrowPathIcon className="text-gray-600 w-5 h-5" />
            </button>
         </div>
         <div className="bg-white border border-gray-200 rounded-lg shadow relative">
            {/* <ChatHeader name={"devlazar"} numberOfMessages={chatMessages.length} /> */}
            <ChatContent messages={chatMessages} />
            <ChatInputBox sendANewMessage={sendANewMessage} />
         </div>
      </div>
   );
};

export default Chat;

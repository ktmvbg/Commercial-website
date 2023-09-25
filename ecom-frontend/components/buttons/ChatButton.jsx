'use client'
import React from 'react';
import { InboxIcon } from '@heroicons/react/24/solid'
import Chat from '../Chat/ChatComponent'

export default function ChatButton() {
    const [showChat, setShowChat] = React.useState(false);

    const toggleChat = () => {
        setShowChat(!showChat);
    }

    return (
        <div>
            <button
                className="fixed z-90 bottom-8 right-8 bg-blue-600 w-20 h-20 rounded-full drop-shadow-lg flex 
            justify-center items-center text-white text-4xl hover:bg-blue-500 transition-all
            "
                onClick={toggleChat}
            >
                <InboxIcon className='h-6 w-6' />
            </button>


                <div hidden={!showChat}>
                    <div className="fixed z-50 bottom-32 right-8 bg-white">
                        <Chat />
                    </div>
                </div>

            
        </div>
    )

}